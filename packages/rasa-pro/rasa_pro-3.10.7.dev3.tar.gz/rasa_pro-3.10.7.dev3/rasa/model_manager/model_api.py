import asyncio
import os
from typing import Any, Dict, Optional
import dotenv
from sanic import Blueprint, Sanic, response
from sanic.response import json
from sanic.exceptions import NotFound
from sanic.request import Request
import structlog
from socketio import AsyncServer

from rasa.model_manager.config import SERVER_BASE_URL
from rasa.model_manager.runner_service import (
    BotSession,
    run_bot,
    terminate_bot,
    update_bot_status,
)
from rasa.model_manager.socket_bridge import create_bridge_client
from rasa.model_manager.trainer_service import (
    TrainingSession,
    run_training,
    terminate_training,
    train_path,
    update_training_status,
)
from rasa.model_manager.utils import (
    logs_base_path,
    logs_path,
    models_base_path,
    models_path,
)

dotenv.load_dotenv()

structlogger = structlog.get_logger()


# A simple in-memory store for training sessions and running bots
trainings: Dict[str, TrainingSession] = {}
running_bots: Dict[str, BotSession] = {}

# A simple in-memory store for active chat connections to studio frontend
socket_proxy_clients = {}


def prepare_working_directories() -> None:
    """Make sure all required directories exist."""
    os.makedirs(logs_base_path(), exist_ok=True)
    os.makedirs(models_base_path(), exist_ok=True)


def cleanup_training_processes() -> None:
    """Terminate all running training processes."""
    structlogger.debug("model_trainer.cleanup_processes.started")
    for training in trainings.values():
        terminate_training(training)


def cleanup_bot_processes() -> None:
    """Terminate all running bot processes."""
    structlogger.debug("model_runner.cleanup_processes.started")
    for bot in running_bots.values():
        terminate_bot(bot)


def update_status_of_all_trainings() -> None:
    """Update the status of all training processes."""
    for training in trainings.values():
        update_training_status(training)


async def update_status_of_all_bots() -> None:
    """Update the status of all bot processes."""
    for bot in running_bots.values():
        await update_bot_status(bot)


def base_server_url(request: Request) -> str:
    """Return the base URL of the server."""
    if SERVER_BASE_URL:
        return SERVER_BASE_URL
    else:
        return f"{request.scheme}://{request.host}"


def get_log_url(request: Request, action_id: str) -> response.HTTPResponse:
    """Return a URL for downloading the log file for training / deployment."""
    if not os.path.exists(logs_path(action_id)):
        return json({"message": "Log not found"}, status=404)

    return json(
        {
            "url": f"{base_server_url(request)}/logs/{action_id}.txt",
            "expires_in_seconds": 60 * 60 * 24,
        }
    )


def get_training_model_url(request: Request, training_id: str) -> response.HTTPResponse:
    """Return a URL for downloading the model file for a training session."""
    if not os.path.exists(f"{train_path(training_id)}/models"):
        return json({"message": "Model not found"}, status=404)

    # pick the first model in the directory, link it to models/
    # and provide the download link
    models = os.listdir(f"{train_path(training_id)}/models")
    if not models:
        return json({"message": "Model not found"}, status=404)

    # there should really be only one model
    model = models[0]

    if not os.path.exists(models_path(model)):
        os.symlink(f"{train_path(training_id)}/models/{model}", models_path(model))

    return json(
        {
            "url": f"{base_server_url(request)}/models/{model}",
            "expires_in_seconds": 60 * 60 * 24,
        }
    )


async def continuously_update_process_status() -> None:
    """Regularly Update the status of all training and bot processes."""
    structlogger.debug("model_api.update_process_status.started")

    while True:
        update_status_of_all_trainings()
        await update_status_of_all_bots()
        await asyncio.sleep(1)


def internal_blueprint() -> Blueprint:
    """Create a blueprint for the model manager API."""
    bp = Blueprint("model_api_internal")

    @bp.before_server_stop
    async def cleanup_processes(app: Sanic, loop: asyncio.AbstractEventLoop) -> None:
        """Terminate all running processes before the server stops."""
        structlogger.debug("model_api.cleanup_processes.started")
        cleanup_training_processes()
        cleanup_bot_processes()

    @bp.get("/")
    async def health(request: Request) -> response.HTTPResponse:
        return json(
            {
                "status": "ok",
                "bots": [
                    {
                        "deployment_id": bot.deployment_id,
                        "status": bot.status,
                        "internal_url": bot.internal_url,
                        "url": bot.url,
                    }
                    for bot in running_bots.values()
                ],
                "trainings": [
                    {
                        "training_id": training.training_id,
                        "assistant_id": training.assistant_id,
                        "client_id": training.client_id,
                        "progress": training.progress,
                        "status": training.status,
                    }
                    for training in trainings.values()
                ],
            }
        )

    @bp.get("/training")
    async def get_training_list(request: Request) -> response.HTTPResponse:
        """Return a list of all training sessions for an assistant."""
        assistant_id = request.args.get("assistant_id")
        sessions = [
            {
                "training_id": session.training_id,
                "assistant_id": session.assistant_id,
                "client_id": session.client_id,
                "training_runtime": "self",
                "status": session.status,
                "bot_config": None,
                "logs": None,
                "metadata": None,
                "model": None,
                "runtime_metadata": None,
            }
            for session in trainings.values()
            if session.assistant_id == assistant_id
        ]
        return json({"training_sessions": sessions, "total_number": len(sessions)})

    @bp.post("/training")
    async def start_training(request: Request) -> response.HTTPResponse:
        """Start a new training session."""
        data = request.json
        training_id: Optional[str] = data.get("id")
        assistant_id: Optional[str] = data.get("assistant_id")
        client_id: Optional[str] = data.get("client_id")

        if training_id in trainings:
            # fail, because there apparently is already a training with this id
            return json({"message": "Training with this id already exists"}, status=409)

        if not assistant_id:
            return json({"message": "Assistant id is required"}, status=400)

        if not training_id:
            return json({"message": "Training id is required"}, status=400)

        try:
            training_session = run_training(
                training_id=training_id,
                assistant_id=assistant_id,
                client_id=client_id,
                data=data,
            )
            trainings[training_id] = training_session
            return json({"training_id": training_id})
        except Exception as e:
            return json({"message": str(e)}, status=500)

    @bp.get("/training/<training_id>")
    async def get_training(request: Request, training_id: str) -> response.HTTPResponse:
        """Return the status of a training session."""
        if training := trainings.get(training_id):
            return json(
                {
                    "training_id": training_id,
                    "assistant_id": training.assistant_id,
                    "client_id": training.client_id,
                    "progress": training.progress,
                    "status": training.status,
                }
            )
        else:
            return json({"message": "Training not found"}, status=404)

    @bp.delete("/training/<training_id>")
    async def stop_training(
        request: Request, training_id: str
    ) -> response.HTTPResponse:
        # this is a no-op if the training is already done
        if not (training := trainings.get(training_id)):
            return json({"message": "Training session not found"}, status=404)

        terminate_training(training)
        return json({"training_id": training_id})

    @bp.get("/training/<training_id>/download_url")
    async def get_training_download_url(
        request: Request, training_id: str
    ) -> response.HTTPResponse:
        # Provide a URL for downloading the training log
        # check object key that is passed in as a query parameter
        key = request.args.get("object_key")
        if "model.tar.gz" in key:
            return get_training_model_url(request, training_id)
        return get_log_url(request, training_id)

    @bp.post("/bot")
    async def start_bot(request: Request) -> response.HTTPResponse:
        data = request.json
        deployment_id: Optional[str] = data.get("deployment_id")
        assumed_model_path: Optional[str] = data.get("model_path")

        if deployment_id in running_bots:
            # fail, because there apparently is already a bot running with this id
            return json(
                {"message": "Bot with this deployment id already exists"}, status=409
            )

        if not deployment_id:
            return json({"message": "Deployment id is required"}, status=400)

        if not assumed_model_path:
            return json({"message": "Model path is required"}, status=400)

        training_id = assumed_model_path.split("/")[-3]
        training_base_path = train_path(training_id)
        if not os.path.exists(f"{training_base_path}/models"):
            return json(
                {"message": "Model not found, for the given training id"},
                status=404,
            )

        base_url_path = base_server_url(request)
        try:
            bot_session = run_bot(deployment_id, training_base_path, base_url_path)
            running_bots[deployment_id] = bot_session
            return json(
                {
                    "deployment_id": deployment_id,
                    "status": bot_session.status,
                    "url": bot_session.url,
                }
            )
        except Exception as e:
            return json({"message": str(e)}, status=500)

    @bp.delete("/bot/<deployment_id>")
    async def stop_bot(request: Request, deployment_id: str) -> response.HTTPResponse:
        bot = running_bots.get(deployment_id)
        if bot is None:
            return json({"message": "Bot not found"}, status=404)

        terminate_bot(bot)

        return json(
            {"deployment_id": deployment_id, "status": bot.status, "url": bot.url}
        )

    @bp.get("/bot/<deployment_id>")
    async def get_bot(request: Request, deployment_id: str) -> response.HTTPResponse:
        bot = running_bots.get(deployment_id)
        if bot is None:
            return json({"message": "Bot not found"}, status=404)

        return json(
            {
                "deployment_id": deployment_id,
                "status": bot.status,
                "url": bot.url,
            }
        )

    @bp.get("/bot/<deployment_id>/download_url")
    async def get_bot_download_url(
        request: Request, deployment_id: str
    ) -> response.HTTPResponse:
        return get_log_url(request, deployment_id)

    @bp.get("/bot/<deployment_id>/logs")
    async def get_bot_logs(
        request: Request, deployment_id: str
    ) -> response.HTTPResponse:
        return get_log_url(request, deployment_id)

    @bp.get("/bot")
    async def list_bots(request: Request) -> response.HTTPResponse:
        bots = [
            {
                "deployment_id": bot.deployment_id,
                "status": bot.status,
                "url": bot.url,
            }
            for bot in running_bots.values()
        ]
        return json({"deployment_sessions": bots, "total_number": len(bots)})

    return bp


def external_blueprint() -> Blueprint:
    """Create a blueprint for the model manager API."""
    from rasa.core.channels.socketio import SocketBlueprint

    sio = AsyncServer(async_mode="sanic", cors_allowed_origins=[])
    bp = SocketBlueprint(sio, "", "model_api_external")

    @bp.route("/logs/<path:path>")
    async def get_training_logs(request: Request, path: str) -> response.HTTPResponse:
        try:
            headers = {"Content-Disposition": 'attachment; filename="log.txt"'}
            return await response.file(
                os.path.join(logs_base_path(), path), headers=headers
            )
        except NotFound:
            return json({"message": "Log not found"}, status=404)

    @bp.route("/models/<path:path>")
    async def send_model(request: Request, path: str) -> response.HTTPResponse:
        try:
            return await response.file(models_path(path))
        except NotFound:
            return json({"message": "Model not found"}, status=404)

    @sio.on("connect")
    async def socketio_websocket_traffic(
        sid: str, environ: Dict, auth: Optional[Dict]
    ) -> bool:
        """Bridge websockets between user chat socket and bot server."""
        structlogger.debug("model_runner.user_connected", sid=sid)
        deployment_id = auth.get("deployment_id") if auth else None

        if deployment_id is None:
            structlogger.error("model_runner.bot_no_deployment_id", sid=sid)
            return False

        bot = running_bots.get(deployment_id)
        if bot is None:
            structlogger.error(
                "model_runner.bot_not_found", deployment_id=deployment_id
            )
            return False

        client = await create_bridge_client(sio, bot.internal_url, sid, deployment_id)

        if client.sid is not None:
            structlogger.debug(
                "model_runner.bot_connection_established", deployment_id=deployment_id
            )
            socket_proxy_clients[sid] = client
            return True
        else:
            structlogger.error(
                "model_runner.bot_connection_failed", deployment_id=deployment_id
            )
            return False

    @sio.on("disconnect")
    async def disconnect(sid: str) -> None:
        structlogger.debug("model_runner.bot_disconnect", sid=sid)
        if sid in socket_proxy_clients:
            await socket_proxy_clients[sid].disconnect()
            del socket_proxy_clients[sid]

    @sio.on("*")
    async def handle_message(event: str, sid: str, data: Dict[str, Any]) -> None:
        # bridge both, incoming messages to the bot_url but also
        # send the response back to the client. both need to happen
        # in parallel in an async way

        client = socket_proxy_clients.get(sid)
        if client is None:
            structlogger.error("model_runner.bot_not_connected", sid=sid)
            return

        await client.emit(event, data)

    return bp

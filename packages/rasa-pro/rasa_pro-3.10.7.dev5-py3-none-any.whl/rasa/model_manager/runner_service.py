import os
import shutil
import aiohttp
import structlog
import subprocess
from dataclasses import dataclass

from rasa.model_manager.config import RASA_PYTHON_PATH, SERVER_BASE_WORKING_DIRECTORY
from rasa.model_manager.utils import logs_path

structlogger = structlog.get_logger()


@dataclass
class BotSession:
    """Store information about a running bot."""

    deployment_id: str
    status: str
    process: subprocess.Popen
    url: str
    internal_url: str
    port: int


def bot_path(deployment_id: str) -> str:
    """Return the path to the bot directory for a given deployment id."""
    return os.path.abspath(f"{SERVER_BASE_WORKING_DIRECTORY}/bots/{deployment_id}")


async def is_bot_startup_finished(bot: BotSession) -> bool:
    """Send a request to the bot to see if the bot is up and running."""
    health_timeout = aiohttp.ClientTimeout(total=5, sock_connect=2, sock_read=3)
    try:
        async with aiohttp.ClientSession(timeout=health_timeout) as session:
            async with session.get(f"{bot.internal_url}/status") as resp:
                return resp.status == 200
    except aiohttp.client_exceptions.ClientConnectorError:
        structlogger.debug(
            "model_runner.bot.not_running_yet", deployment_id=bot.deployment_id
        )
        return False


def update_bot_to_stopped(bot: BotSession) -> None:
    """Set a bots state to stopped."""
    structlogger.info(
        "model_runner.bot_stopped",
        deployment_id=bot.deployment_id,
        status=bot.process.returncode,
    )
    bot.status = "stopped"


def update_bot_to_running(bot: BotSession) -> None:
    """Set a bots state to running."""
    structlogger.info(
        "model_runner.bot_running",
        deployment_id=bot.deployment_id,
    )
    bot.status = "running"


def get_open_port() -> int:
    """Get an open port on the system that is not in use yet."""
    # from https://stackoverflow.com/questions/2838244/get-open-tcp-port-in-python/2838309#2838309
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


def prepare_bot_directory(bot_base_path: str, training_base_path: str) -> None:
    """Prepare the bot directory for a new bot session."""
    if not os.path.exists(bot_base_path):
        os.makedirs(bot_base_path, exist_ok=True)
    else:
        shutil.rmtree(bot_base_path, ignore_errors=True)

    shutil.copytree(f"{training_base_path}/models", f"{bot_base_path}/models")

    try:
        shutil.copy(
            f"{training_base_path}/endpoints.yml", f"{bot_base_path}/endpoints.yml"
        )
    except FileNotFoundError:
        structlogger.warning("model_runner.bot.prepare.no_endpoints")

    try:
        shutil.copy(
            f"{training_base_path}/credentials.yml", f"{bot_base_path}/credentials.yml"
        )
    except FileNotFoundError:
        structlogger.warning("model_runner.bot.prepare.no_credentials")


def start_bot_process(
    deployment_id: str, bot_base_path: str, base_url_path: str
) -> BotSession:
    port = get_open_port()
    log_path = logs_path(deployment_id)

    process = subprocess.Popen(
        [
            RASA_PYTHON_PATH,
            "-m",
            "rasa.__main__",
            "run",
            "--endpoints",
            f"{bot_base_path}/endpoints.yml",
            "--credentials",
            f"{bot_base_path}/credentials.yml",
            "--enable-api",
            "--debug",
            f"--port={port}",
            "--cors",
            "*",
            # absolute path to models as positional arg
            f"{bot_base_path}/models",
        ],
        cwd=bot_base_path,
        stdout=open(log_path, "w"),
        stderr=subprocess.STDOUT,
        env=os.environ.copy(),
    )

    internal_bot_url = f"http://localhost:{port}"

    structlogger.info(
        "model_runner.bot.starting",
        deployment_id=deployment_id,
        log=log_path,
        url=internal_bot_url,
        port=port,
        pid=process.pid,
    )

    return BotSession(
        deployment_id=deployment_id,
        status="queued",
        process=process,
        url=f"{base_url_path}?deployment_id={deployment_id}",
        internal_url=internal_bot_url,
        port=port,
    )


def run_bot(
    deployment_id: str, training_base_path: str, base_url_path: str
) -> BotSession:
    """Deploy a bot based on a given training id."""
    bot_base_path = bot_path(deployment_id)
    prepare_bot_directory(bot_base_path, training_base_path)

    return start_bot_process(deployment_id, bot_base_path, base_url_path)


async def update_bot_status(bot: BotSession) -> None:
    """Update the status of a bot based on the process return code."""
    if bot.status == "running" and bot.process.poll() is not None:
        update_bot_to_stopped(bot)
    if bot.status == "queued" and await is_bot_startup_finished(bot):
        update_bot_to_running(bot)


def terminate_bot(bot: BotSession) -> None:
    """Terminate the bot process."""
    if bot.status in {"running", "queued"}:
        try:
            bot.process.terminate()
            structlogger.info(
                "model_runner.stopping_bot",
                deployment_id=bot.deployment_id,
                status=bot.process.returncode,
            )
            bot.status = "stopped"
        except ProcessLookupError:
            structlogger.debug(
                "model_runner.stop_bot.process_not_found",
                deployment_id=bot.deployment_id,
            )

from typing import Any, Dict
from socketio import AsyncServer
import structlog
from socketio.asyncio_client import AsyncClient


structlogger = structlog.get_logger()


async def create_bridge_client(
    sio: AsyncServer, url: str, sid: str, deployment_id: str
) -> AsyncClient:
    """Create a new socket bridge client."""
    client = AsyncClient()

    await client.connect(url)

    @client.event  # type: ignore[misc]
    async def session_confirm(data: Dict[str, Any]) -> None:
        structlogger.debug(
            "model_runner.bot_session_confirmed", deployment_id=deployment_id
        )
        await sio.emit("session_confirm", room=sid)

    @client.event  # type: ignore[misc]
    async def bot_message(data: Dict[str, Any]) -> None:
        structlogger.debug("model_runner.bot_message", deployment_id=deployment_id)
        await sio.emit("bot_message", data, room=sid)

    @client.event  # type: ignore[misc]
    async def disconnect() -> None:
        structlogger.debug(
            "model_runner.bot_connection_closed", deployment_id=deployment_id
        )
        await sio.emit("disconnect", room=sid)

    @client.event  # type: ignore[misc]
    async def connect_error() -> None:
        structlogger.error(
            "model_runner.bot_connection_error", deployment_id=deployment_id
        )
        await sio.emit("disconnect", room=sid)

    return client

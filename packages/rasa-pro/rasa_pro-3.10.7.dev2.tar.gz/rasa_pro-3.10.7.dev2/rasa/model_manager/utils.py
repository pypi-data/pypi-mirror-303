import os

from rasa.model_manager.config import SERVER_BASE_WORKING_DIRECTORY


def logs_base_path() -> str:
    """Return the path to the logs directory."""
    return os.path.abspath(f"{SERVER_BASE_WORKING_DIRECTORY}/logs")


def models_base_path() -> str:
    """Return the path to the models directory."""
    return os.path.abspath(f"{SERVER_BASE_WORKING_DIRECTORY}/models")


def logs_path(action_id: str) -> str:
    """Return the path to the log file for a given action id.

    Args:
        action_id: can either be a training_id or a deployment_id
    """
    return os.path.abspath(f"{logs_base_path()}/{action_id}.txt")


def models_path(training_id: str) -> str:
    """Return the path to the models directory for a given training id."""
    return os.path.abspath(f"{models_base_path()}/{training_id}")

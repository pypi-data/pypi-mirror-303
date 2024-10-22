import os
from typing import Any, Dict, Optional
import shutil
import base64
import structlog
import subprocess
from dataclasses import dataclass

from rasa.model_manager.config import RASA_PYTHON_PATH, SERVER_BASE_WORKING_DIRECTORY
from rasa.model_manager.utils import logs_path

structlogger = structlog.get_logger()


@dataclass
class TrainingSession:
    """Store information about a training session."""

    training_id: str
    assistant_id: str
    client_id: Optional[str]
    progress: int
    status: str
    process: subprocess.Popen


def train_path(training_id: str) -> str:
    """Return the path to the training directory for a given training id."""
    return os.path.abspath(f"{SERVER_BASE_WORKING_DIRECTORY}/trainings/{training_id}")


def cache_for_assistant_path(assistant_id: str) -> str:
    """Return the path to the cache directory for a given assistant id."""
    return os.path.abspath(f"{SERVER_BASE_WORKING_DIRECTORY}/caches/{assistant_id}")


def write_encoded_data_to_file(encoded_data: bytes, file: str) -> None:
    """Write base64 encoded data to a file."""
    # create the directory if it does not exist of the parent directory
    os.makedirs(os.path.dirname(file), exist_ok=True)

    with open(file, "w") as f:
        decoded = base64.b64decode(encoded_data)
        text = decoded.decode("utf-8")
        f.write(text)


def terminate_training(training: TrainingSession) -> None:
    if training.status == "running":
        structlogger.info(
            "model_trainer.user_stopping_training", training_id=training.training_id
        )
        try:
            training.process.terminate()
            training.status = "stopped"
        except ProcessLookupError:
            structlogger.debug(
                "model_trainer.training_process_not_found",
                training_id=training.training_id,
            )


def update_training_status(training: TrainingSession) -> None:
    if training.status != "running":
        # skip if the training is not running
        return
    if training.process.poll() is None:
        # process is still running
        return

    complete_training(training)


def complete_training(training: TrainingSession) -> None:
    """Complete a training session.

    Transitions the status of a training process to "done" if the process has
    finished successfully, and to "error" if the process has finished with an
    error.
    """
    training.status = "done" if training.process.returncode == 0 else "error"
    training.progress = 100

    structlogger.info(
        "model_trainer.training_finished",
        training_id=training.training_id,
        status=training.status,
    )

    # persist the assistant cache to speed up future training runs for this
    # assistant
    persist_rasa_cache(training.assistant_id, train_path(training.training_id))


def seed_training_directory_with_rasa_cache(
    training_base_path: str, assistant_id: str
) -> None:
    """Populate the training directory with the cache of a previous training."""
    # check if there is a cache for this assistant
    cache_path = cache_for_assistant_path(assistant_id)

    if os.path.exists(cache_path):
        structlogger.debug(
            "model_trainer.populating_training_dir_with_cache",
            assistant_id=assistant_id,
            training_base_path=training_base_path,
        )
        # copy the cache to the training directory
        shutil.copytree(cache_path, f"{training_base_path}/.rasa")


def persist_rasa_cache(assistant_id: str, training_base_path: str) -> None:
    """Persist the cache of a training session to speed up future trainings."""
    # copy the cache from the training directory to the cache directory
    # cache files are stored inside of `/.rasa/` of the training folder
    structlogger.debug(
        "model_trainer.persisting_assistant_cache", assistant_id=assistant_id
    )
    cache_path = cache_for_assistant_path(assistant_id)
    # clean up the cache directory first
    shutil.rmtree(cache_path, ignore_errors=True)
    shutil.copytree(f"{training_base_path}/.rasa", cache_path)


def write_training_data_to_files(
    encoded_training_data: Dict[str, Any], training_base_path: str
) -> None:
    """Write the training data to files in the training directory.

    Incoming data format, all keys being optional:
    ````
    {
        "domain": "base64 encoded domain.yml",
        "credentials": "base64 encoded credentials.yml",
        "endpoints": "base64 encoded endpoints.yml",
        "flows": "base64 encoded flows.yml",
        "config": "base64 encoded config.yml",
        "stories": "base64 encoded stories.yml",
        "rules": "base64 encoded rules.yml",
        "nlu": "base64 encoded nlu.yml"
    }
    ```
    """
    data_to_be_written_to_files = {
        "domain": "domain.yml",
        "credentials": "credentials.yml",
        "endpoints": "endpoints.yml",
        "flows": "data/flows.yml",
        "config": "config.yml",
        "stories": "data/stories.yml",
        "rules": "data/rules.yml",
        "nlu": "data/nlu.yml",
    }

    for key, file in data_to_be_written_to_files.items():
        write_encoded_data_to_file(
            encoded_training_data.get(key, ""),
            f"{training_base_path}/{file}",
        )


def prepare_training_directory(
    training_base_path: str, assistant_id: str, data: Dict[str, Any]
) -> None:
    """Prepare the training directory for a new training session."""
    encoded_training_data = data.get("bot_config", {}).get("data", {})

    # create a new working directory and store the training data from the
    # request there. the training data in the request is base64 encoded
    os.makedirs(training_base_path, exist_ok=True)

    seed_training_directory_with_rasa_cache(training_base_path, assistant_id)
    write_training_data_to_files(encoded_training_data, training_base_path)


def start_training_process(
    training_id: str, assistant_id: str, client_id: str, training_base_path: str
) -> TrainingSession:
    log_path = logs_path(training_id)

    # Start the training in a subprocess
    # set the working directory to the training directory
    # run the rasa train command as a subprocess, activating poetry before running
    # pipe the stdout and stderr to the same file
    process = subprocess.Popen(
        [
            RASA_PYTHON_PATH,
            "-m",
            "rasa.__main__",
            "train",
            "--debug",
            "--out",
            f"{training_base_path}/models",
            "--data",
            f"{training_base_path}/data",
            "--config",
            f"{training_base_path}/config.yml",
            "--domain",
            f"{training_base_path}/domain.yml",
            "--endpoints",
            f"{training_base_path}/endpoints.yml",
        ],
        cwd=training_base_path,
        stdout=open(log_path, "w"),
        stderr=subprocess.STDOUT,
        env=os.environ.copy(),
    )

    structlogger.info(
        "model_trainer.training_started",
        training_id=training_id,
        assistant_id=assistant_id,
        client_id=client_id,
        log=log_path,
        pid=process.pid,
    )

    return TrainingSession(
        training_id=training_id,
        assistant_id=assistant_id,
        client_id=client_id,
        progress=0,
        status="running",
        process=process,  # Store the process handle
    )


def run_training(
    training_id: str, assistant_id: str, client_id: str, data: Dict
) -> TrainingSession:
    """Run a training session."""
    training_base_path = train_path(training_id)

    prepare_training_directory(training_base_path, assistant_id, data)
    return start_training_process(
        training_id=training_id,
        assistant_id=assistant_id,
        client_id=client_id,
        training_base_path=training_base_path,
    )

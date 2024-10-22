import os
import logging

import structlog

from rasa.model_manager import model_api
from rasa.utils.common import configure_logging_and_warnings
import rasa.utils.licensing

structlogger = structlog.get_logger()

MODEL_SERVICE_PORT = 8000


def main() -> None:
    """Start the Rasa Model Manager server.

    The API server can receive requests to train models, run bots, and manage
    the lifecycle of models and bots.
    """
    model_api.prepare_working_directories()

    configure_logging_and_warnings(
        log_level=logging.DEBUG,
        logging_config_file=None,
        warn_only_once=True,
        filter_repeated_logs=True,
    )

    rasa.utils.licensing.validate_license_from_env()
    # assert that an openai api key is set
    assert (
        "OPENAI_API_KEY" in os.environ
    ), "Please set the OPENAI_API_KEY environment variable"

    structlogger.debug("model_training.starting_server", port=MODEL_SERVICE_PORT)
    structlogger.debug("model_running.starting_server", port=MODEL_SERVICE_PORT)

    model_api.app.add_task(model_api.continuously_update_process_status)
    model_api.app.run(host="0.0.0.0", port=MODEL_SERVICE_PORT, legacy=True)


if __name__ == "__main__":
    main()

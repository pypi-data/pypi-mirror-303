import sys
import os

SERVER_BASE_WORKING_DIRECTORY = os.environ.get(
    "RASA_MODEL_SERVER_BASE_DIRECTORY", "working-data"
)

SERVER_BASE_URL = os.environ.get("RASA_MODEL_SERVER_BASE_URL", None)

# The path to the python executable that is running this script
# we will use the same python to run training / bots
RASA_PYTHON_PATH = sys.executable

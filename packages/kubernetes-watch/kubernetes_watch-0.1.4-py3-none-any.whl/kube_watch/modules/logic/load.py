import os
from prefect import get_run_logger
logger = get_run_logger()

def load_secrets_to_env(data):
    for key, value in data.items():
        os.environ[key] = value
        # logger.info(f"ENV VAR: {key} loaded")

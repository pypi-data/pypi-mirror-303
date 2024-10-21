import os

import yaml
from loguru import logger
from rich.console import Console

console = Console()


def list_yaml_files(directory: str) -> list[str]:
    logger.info(f"Listing YAML files in directory: {directory}")
    if not os.path.exists(directory):
        logger.error(f"Directory does not exist: {directory}")
        return []
    return [f for f in os.listdir(directory) if f.endswith((".yaml", ".yml"))]


def load_yaml_data(file_path: str) -> dict:
    logger.info(f"Loading YAML data from: {file_path}")
    try:
        with open(file_path) as file:
            return yaml.safe_load(file)
    except Exception as e:
        logger.error(f"Error loading YAML file: {e}")
        raise ValueError(f"Error loading YAML file: {e}")

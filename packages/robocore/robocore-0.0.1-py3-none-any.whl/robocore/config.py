import yaml
import logging
from .utils import get_logger

logger = get_logger(__name__)

def load_config(config_file):
    """
    Load configuration from a YAML file.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    logger.info(f"Configuration loaded from '{config_file}'.")
    return config

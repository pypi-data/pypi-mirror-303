import logging
import os
import pathlib

_SILVERRIVER_CONFIG_FILE = pathlib.Path.home() / ".config" / "silverriver" / "auth"
logger = logging.getLogger(__name__)


def store_silverriver_key(api_key: str):
    _SILVERRIVER_CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    _SILVERRIVER_CONFIG_FILE.write_text(api_key.strip())
    logger.info("API token saved at %s", _SILVERRIVER_CONFIG_FILE)


def read_silverriver_key():
    api_key = os.getenv("CRUX_API_KEY")
    if not api_key:
        try:
            api_key = _SILVERRIVER_CONFIG_FILE.read_text().strip()
        except FileNotFoundError:
            raise ValueError(
                "API key not found. Please set it using the auth command or via the CRUX_API_KEY environment variable.")
    return api_key

import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


def get_required_env_variable(name: str) -> str:
    """Return an environment variable or raise a clear error."""
    value = os.getenv(name)

    if not value or not value.strip():
        raise ValueError(
            f"Missing required environment variable: {name}. "
            f"Create a .env file from .env.example and set '{name}'."
        )

    return value.strip()


OLLAMA_API_BASE = get_required_env_variable("OLLAMA_API_BASE")
OLLAMA_MODEL = get_required_env_variable("OLLAMA_MODEL")

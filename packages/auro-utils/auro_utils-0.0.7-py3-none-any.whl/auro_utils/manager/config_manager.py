import os
import json
import toml
from typing import Any, Dict, Union


def load_config(
    config: Union[str, dict], relative_to: str = None, file_type: str = "toml"
) -> dict:
    """
    Load configuration from a file or a dictionary.

    Args:
        config (Union[str, dict]):
            Path to the config file or a dict with config data.
        relative_to (str, optional):
            Base directory for resolving relative paths.
        file_type (str, optional):
            Type of config file ('toml' or 'json').

    Returns:
        dict:
            Loaded configuration data.

    Raises:
        ValueError: For invalid config paths, unsupported file types, or invalid config types.
    """
    if isinstance(config, str):
        # Check suffix
        if not config.endswith(f".{file_type}"):
            raise ValueError(f"Config file must be a {file_type.lower()} file.")
        # Create the absolute path
        config_path = (
            os.path.join(relative_to, config.lstrip("/")) if relative_to else config
        )
        # Check if the file exists
        if not os.path.isfile(config_path):
            raise ValueError(f"Config file does not exist: {config_path}")
        # Load the config
        if file_type == "toml":
            return toml.load(config_path)
        elif file_type == "json":
            return json.load(open(config_path, "r", encoding="utf-8"))
        else:
            raise ValueError(f"Unsupported config file type: {file_type}")

    elif isinstance(config, dict):
        return config
    else:
        raise ValueError("Invalid config type")


def save_config(
    config: Union[str, dict],
    path: str,
    relative_to: str = None,
    file_type: str = "toml",
) -> None:
    """
    Save configuration to a file or a dictionary.

    Args:
        config (Union[str, dict]):
            Config data to save. Can be a dictionary or a path to a config file.
        path (str):
            Path where the config file will be saved.
        relative_to (str, optional):
            Base directory for resolving relative paths.
        file_type (str, optional):
            Type of config file ('toml' or 'json').

    Raises:
        ValueError: For unsupported file types, invalid config types, or invalid paths.
    """
    if not isinstance(config, dict):
        raise ValueError("Config must be a dictionary.")

    # Create the absolute path for saving
    save_path = os.path.join(relative_to, path.lstrip("/")) if relative_to else path

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save the config
    if file_type == "toml":
        with open(save_path, "w", encoding="utf-8") as f:
            toml.dump(config, f)
    elif file_type == "json":
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
    else:
        raise ValueError(f"Unsupported config file type: {file_type}")

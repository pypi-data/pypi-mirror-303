# System
import inspect
from typing import Any, Dict, List, Union
from datetime import datetime
import os

# File
import pickle
import json
import toml
import h5py

# Math
import numpy as np

from .file_manager import check_file_exists
from .file_manager import ensure_path_exists


def read_pickle(file_path: str) -> Dict[str, Any]:
    """
    Load data from a Pickle file.

    Args:
        file_path (str): The path to the Pickle file.

    Returns:
        dict: Data loaded from the Pickle file.

    Raises:
        ValueError: If there is an error during loading.
    """
    check_file_exists(file_path)
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        raise ValueError(f"Error reading Pickle file {file_path}") from e


def write_pickle(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to a Pickle file.

    Args:
        data (dict): Data to be saved.
        file_path (str): The path to the Pickle file.

    Raises:
        ValueError: If there is an error during saving.
    """
    ensure_path_exists(file_path)
    try:
        with open(file_path, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        raise ValueError(f"Error writing to Pickle file {file_path}") from e


def read_json(file_path: str) -> Dict[str, Any]:
    """
    Load data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: Parsed JSON data.

    Raises:
        ValueError: If there is an error during loading.
    """
    check_file_exists(file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Error reading JSON file '{file_path}': {e}") from e


def write_json(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to a JSON file.

    Args:
        data (dict): Data to be saved.
        file_path (str): The path to the JSON file.

    Raises:
        ValueError: If there is an error during saving.
    """
    ensure_path_exists(file_path)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error writing JSON to {file_path}: {e}") from e


def read_toml(file_path: str) -> Dict[str, Any]:
    """
    Load data from a TOML file.

    Args:
        file_path (str): The path to the TOML file.

    Returns:
        dict: Parsed TOML data.

    Raises:
        ValueError: If there is an error during loading.
    """
    check_file_exists(file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return toml.load(f)
    except toml.TomlDecodeError as e:
        raise ValueError(f"Error decoding TOML from {file_path}: {e}") from e


def write_toml(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to a TOML file.

    Args:
        data (dict): Data to be saved.
        file_path (str): The path to the TOML file.

    Raises:
        ValueError: If there is an error during saving.
    """
    ensure_path_exists(file_path)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            toml.dump(data, f)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error writing TOML to {file_path}: {e}") from e


def read_hdf5(file_path: str) -> Dict[str, Any]:
    """
    Load data from an HDF5 file.

    Args:
        file_path (str): The path to the HDF5 file.

    Returns:
        dict: Data loaded from the HDF5 file.

    Raises:
        ValueError: If there is an error during loading.
    """
    check_file_exists(file_path)
    data = {}
    try:
        with h5py.File(file_path, "r") as f:
            for key in f:
                data[key] = np.array(f[key])
    except Exception as e:
        raise ValueError(f"Error reading HDF5 file {file_path}: {e}") from e
    return data


def write_hdf5(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to an HDF5 file.

    Args:
        data (dict): Data to be saved, with values as numpy arrays.
        file_path (str): The path to the HDF5 file.

    Raises:
        ValueError: If there is an error during saving.
    """
    ensure_path_exists(file_path)
    try:
        with h5py.File(file_path, "w") as f:
            for key, value in data.items():
                f.create_dataset(key, data=value)
    except Exception as e:
        raise ValueError(f"Error writing to HDF5 file {file_path}: {e}") from e


def split_list_into_batches(
    list_to_split: List[Any], batch_size: int, delete_last_one: bool = False
) -> List[List[Any]]:
    """Split a list into batches of a specified size.

    Args:
        list_to_split (list): The list to be split.
        batch_size (int): The size of each batch.
        delete_last_one (bool): Flag to delete the last batch if smaller than batch_size.

    Returns:
        list: A list of batches.
    """
    batches = [
        list_to_split[i : i + batch_size]
        for i in range(0, len(list_to_split), batch_size)
    ]
    if delete_last_one and len(batches[-1]) < batch_size:
        batches.pop()
    return batches


def get_list_segment(
    lst: List[Any], main_index: int, left_buffer: int, right_buffer: int
) -> List[Any]:
    """Get a segment from a list around a specified main index with buffers.

    Args:
        lst (list): The list from which to extract the segment.
        main_index (int): The index around which the segment is centered.
        left_buffer (int): Elements to include to the left of main_index.
        right_buffer (int): Elements to include to the right of main_index.

    Returns:
        list: A segment of the list centered around main_index.
    """
    length = len(lst)
    left_indices = [(main_index - i) % length for i in range(1, left_buffer + 1)]
    right_indices = [(main_index + i) % length for i in range(1, right_buffer + 1)]
    return (
        [lst[idx] for idx in left_indices[::-1]]
        + [lst[main_index]]
        + [lst[idx] for idx in right_indices]
    )

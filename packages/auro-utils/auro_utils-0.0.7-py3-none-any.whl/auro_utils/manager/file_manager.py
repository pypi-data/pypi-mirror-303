import os
import inspect
from datetime import datetime
import rospkg


def check_file_exists(file_path: str) -> None:
    """Check if the specified file exists.

    Args:
        file_path (str): Path to the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")


def ensure_path_exists(path: str) -> None:
    """Ensure that the given path exists.

    Args:
        path (str): Path to the file or directory.
    """
    # Determine if the path is a file or a directory
    if os.path.isfile(path) or os.path.splitext(path)[1]:
        # If it's a file, get the directory containing the file
        dir_path = os.path.dirname(path)
    else:
        # If it's a directory, use the path as is
        dir_path = path

    # Create the directory if it doesn't exist
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)


def get_project_top_level_dir() -> str:
    """Get the top-level directory of the Python project containing the current file.

    Returns:
        str: Absolute path to the top-level directory of the Python project package.
    """
    stack = inspect.stack()
    caller_frame = stack[1]
    caller_file_path = os.path.abspath(caller_frame.filename)
    directory = os.path.dirname(caller_file_path)
    while os.path.exists(os.path.join(directory, "__init__.py")):
        directory = os.path.dirname(directory)
    return directory


def find_ros_package(package_name: str) -> str:
    """Find the path of a ROS package.

    Args:
        package_name (str): The name of the ROS package.

    Returns:
        str: Path to the ROS package.
    """
    return rospkg.RosPack().get_path(package_name)


def get_current_system_time() -> str:
    """Get the current system time in 'YYYYMMDDHHMMSS' format.

    Returns:
        str: Current system time string.
    """
    current_time = datetime.now()
    return current_time.strftime("%Y%m%d%H%M%S")

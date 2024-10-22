import numpy as np
from typing import List, Union, Tuple


def xyzw_to_wxyz(
    quaternion: Union[List[float], np.ndarray]
) -> Union[List[float], np.ndarray]:
    """Convert quaternion from [x, y, z, w] to [w, x, y, z].

    Args:
        quaternion:
            quaternion in format of [x, y, z, w]

    Returns:
        quaternion:
            quaternion in format of [w, x, y, z]
    """
    if isinstance(quaternion, np.ndarray):
        return np.array([quaternion[3], quaternion[0], quaternion[1], quaternion[2]])
    return [quaternion[3], quaternion[0], quaternion[1], quaternion[2]]


def wxzy_to_xyzw(
    quaternion: Union[List[float], np.ndarray]
) -> Union[List[float], np.ndarray]:
    """Convert quaternion from [w, x, y, z] to [x, y, z, w].

    Args:
        quaternion:
            quaternion in format of [w, x, y, z]

    Returns:
        quaternion:
            quaternion in format of [x, y, z, w]
    """
    if isinstance(quaternion, np.ndarray):
        return np.array([quaternion[1], quaternion[2], quaternion[3], quaternion[0]])
    return [quaternion[1], quaternion[2], quaternion[3], quaternion[0]]


def position_and_orientation_to_pose(
    position: Union[List[float], np.ndarray],
    orientation: Union[List[float], np.ndarray],
) -> Union[List[float], np.ndarray]:
    """Convert position and orientation to pose.

    Args:
        position:
            position in format of [x, y, z]
        orientation:
            orientation in format of [x, y, z, w]

    Returns:
        pose:
            pose in format of [x, y, z, w, x, y, z, w]
    """
    if isinstance(position, np.ndarray) or isinstance(orientation, np.ndarray):
        return np.concatenate((position, orientation))
    return position + orientation


def pose_to_position_and_orientation(
    pose: Union[List[float], np.ndarray],
) -> Tuple[Union[List[float], np.ndarray], Union[List[float], np.ndarray]]:
    """Convert pose to position and orientation.

    Args:
        pose:
            pose in format of [x, y, z, w, x, y, z, w]

    Returns:
        position:
            position in format of [x, y, z]
        orientation:
            orientation in format of [x, y, z, w]
    """
    if isinstance(pose, np.ndarray):
        position = pose[:3]
        orientation = pose[
            3:7
        ]  # Assuming the orientation is stored in the next 4 elements
        return position, orientation
    return pose[:3], pose[3:7]  # Split into position and orientation

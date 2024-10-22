"""Common module."""
from enum import Enum
import typing

class PathType(Enum):
    """
    This enum specifies how a path should be interpreted.
    """

    Absolute = 1
    RelativeToProject = 2


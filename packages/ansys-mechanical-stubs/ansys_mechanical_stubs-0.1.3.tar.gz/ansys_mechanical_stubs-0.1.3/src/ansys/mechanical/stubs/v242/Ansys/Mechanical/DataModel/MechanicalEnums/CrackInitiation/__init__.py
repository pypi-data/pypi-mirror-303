"""CrackInitiation module."""
from enum import Enum
import typing

class CrackCenter(Enum):
    """
    This enum specifies the crack center type.
    """

    Manual = 1
    ProgramControlled = 0

class CrackOrientation(Enum):
    """
    This enum specifies the crack orientation type.
    """

    ManualAxesOnly = 2
    ManualCenterAndAxis = 1
    ProgramControlled = 0

class CrackShape(Enum):
    """
    This enum specifies the crack shape type.
    """

    ManualElliptical = 1
    ProgramControlledElliptical = 0


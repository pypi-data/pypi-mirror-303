"""BoundaryConditions module."""
from enum import Enum
import typing

class DataRepresentation(Enum):
    """
    enumeration used to set the return object for the magnitude property in boundary conditions.
    """

    Field = 1
    Flexible = 2


"""ExternalModel module."""
from enum import Enum
import typing

class ImportedSurfaceLoadType(Enum):
    """
    Specifies the ImportedSurfaceLoadType.
    """

    Pressure = 1
    HeatFlux = 22
    Convection = 23


"""SolverData module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class MAPDLAMSupportData(object):
    """
    MAPDLAMSupportData class.
    """

    @property
    def RealConstantId(self) -> typing.Optional[int]:
        """
        Gets the Real Constant Id for the AM Support.
        """
        return None

    @property
    def MaterialIds(self) -> typing.Optional[typing.Iterable[int]]:
        """
        Gets the Material Ids for the AM Support.
        """
        return None


class MAPDLBeamData(object):
    """
    MAPDLBeamData class.
    """

    @property
    def MaterialId(self) -> typing.Optional[int]:
        """
        Gets the Material Id number for the beam connection.
        """
        return None

    @property
    def ElementId(self) -> typing.Optional[int]:
        """
        Gets the Element number for the object.
        """
        return None

    @property
    def RealConstantId(self) -> typing.Optional[int]:
        """
        Gets the Real Constant Id number for the object.
        """
        return None


class MAPDLBearingData(object):
    """
    MAPDLBearingData class.
    """

    @property
    def ElementId(self) -> typing.Optional[int]:
        """
        Gets the Element number for the object.
        """
        return None

    @property
    def RealConstantId(self) -> typing.Optional[int]:
        """
        Gets the Real Constant Id number for the object.
        """
        return None


class MAPDLBodyData(object):
    """
    MAPDLBodyData class.
    """

    @property
    def ElementTypeIds(self) -> typing.Optional[typing.Iterable[int]]:
        """
        Gets the Element Type Ids for the body.
        """
        return None

    @property
    def MaterialIds(self) -> typing.Optional[typing.Iterable[int]]:
        """
        Gets the Material Ids for the body.
        """
        return None

    @property
    def RealConstantId(self) -> typing.Optional[int]:
        """
        Gets the Real Constant Id for the body.
        """
        return None


class MAPDLBoltPretensionData(object):
    """
    MAPDLBoltPretensionData class.
    """

    @property
    def PretensionNodeIds(self) -> typing.Optional[typing.Iterable[int]]:
        """
        Gets the Pretension Node Ids for the bolt pretension.
        """
        return None

    @property
    def RealConstantIds(self) -> typing.Optional[typing.Iterable[int]]:
        """
        Gets the Real Constant Ids for the bolt pretension.
        """
        return None


class MAPDLContactData(object):
    """
    MAPDLContactData class.
    """

    @property
    def SourceId(self) -> typing.Optional[int]:
        """
        Gets the Source Id of the Contact region.
        """
        return None

    @property
    def TargetId(self) -> typing.Optional[int]:
        """
        Gets the Target Id of the Contact region.
        """
        return None


class MAPDLCoordinateSystemData(object):
    """
    MAPDLCoordinateSystemData class.
    """

    @property
    def SystemId(self) -> typing.Optional[int]:
        """
        Gets the System Id for the coordinate system.
        """
        return None


class MAPDLImportedSurfaceLoadData(object):
    """
    MAPDLImportedSurfaceLoadData class.
    """

    @property
    def LoadTypes(self) -> typing.Optional[typing.Iterable[Ansys.Mechanical.DataModel.Enums.ExternalModel.ImportedSurfaceLoadType]]:
        """
        
            Gets the load types present in the row.
            
        """
        return None

    def GetSurfaceEffectElementTypeId(self, eType: Ansys.Mechanical.DataModel.Enums.ExternalModel.ImportedSurfaceLoadType) -> int:
        """
        
            Gets the SurfaceEffectElementTypeId for the requested load type present in the row
            
        """
        pass


class MAPDLJointData(object):
    """
    MAPDLJointData class.
    """

    @property
    def ElementId(self) -> typing.Optional[int]:
        """
        Gets the Element number for the object.
        """
        return None

    @property
    def RealConstantId(self) -> typing.Optional[int]:
        """
        Gets the Real Constant Id number for the object.
        """
        return None


class MAPDLLayeredSectionData(object):
    """
    MAPDLLayeredSectionData class.
    """

    @property
    def SectionId(self) -> typing.Optional[int]:
        """
        Gets the section Id for the layered section.
        """
        return None


class MAPDLRemotePointData(object):
    """
    MAPDLRemotePointData class.
    """

    @property
    def NodeId(self) -> typing.Optional[int]:
        """
        Gets the Pilot Node Id number for the remote point.
        """
        return None


class MAPDLSolverData(object):
    """
    MAPDLSolverData class.
    """

    @property
    def MaxElementId(self) -> typing.Optional[int]:
        """
        Gets the Maximum Element Id number.
        """
        return None

    @property
    def MaxNodeId(self) -> typing.Optional[int]:
        """
        Gets the Maximum Node Id number.
        """
        return None

    @property
    def MaxElementTypeId(self) -> typing.Optional[int]:
        """
        Gets the Maximum Element Type Id number.
        """
        return None

    def GetObjectData(self, obj: Ansys.Mechanical.DataModel.Interfaces.IDataModelObject) -> typing.Any:
        """
        GetObjectData method.
        """
        pass

    def ElementIdsByMaterialId(self, matId: str) -> int:
        """
        Returns a list of Element IDs that belong to a given Material ID
        """
        pass

    def NodeIdsByMaterialId(self, matId: str) -> int:
        """
        Returns a list of Node IDs that belong to a given Material ID
        """
        pass


class MAPDLSpringData(object):
    """
    MAPDLSpringData class.
    """

    @property
    def ElementId(self) -> typing.Optional[int]:
        """
        Gets the Element number for the object.
        """
        return None

    @property
    def RealConstantId(self) -> typing.Optional[int]:
        """
        Gets the Real Constant Id number for the object.
        """
        return None


class MAPDLSurfaceCoatingData(object):
    """
    MAPDLSurfaceCoatingData class.
    """

    @property
    def MaterialId(self) -> typing.Optional[int]:
        """
        Gets the Material Id number for the surface coating.
        """
        return None


class MAPDLSurfaceLoadData(object):
    """
    MAPDLSurfaceLoadData class.
    """

    @property
    def SurfaceEffectElementTypeId(self) -> typing.Optional[int]:
        """
        Gets the Surface Effect Element Type Id used by the load.
        """
        return None


class SolverData(object):
    """
    SolverData class.
    """

    def GetObjectData(self, obj: Ansys.Mechanical.DataModel.Interfaces.IDataModelObject) -> typing.Any:
        """
        Gets the object data.
        """
        pass



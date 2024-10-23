from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel
from moapy.data_pre import Force, Lcom

class ResultMD(MBaseModel):
    """
    Result Markdown
    """
    md: str = dataclass_field(default="", description="Markdown")

    class Config(MBaseModel.Config):
        title = "Markdown"

class ResultBytes(MBaseModel):
    """
    Result Bytes
    """
    type: str = dataclass_field(default="xlsx", description="Type")
    result: str = dataclass_field(default="", description="have to base64 to binary data")

    class Config(MBaseModel.Config):
        title = "Bytes"

class Mesh3DPM(MBaseModel):
    """
    3D P-M onion mesh result class

    Args:
        mesh3dpm (list[Force]): onion mesh result
    """
    mesh3dpm : list[Force] = dataclass_field(default=[], description="onion mesh result")

    class Config(MBaseModel.Config):
        title = "3DPM onion mesh result"

class Result3DPM(MBaseModel):
    """
    GSD 3DPM result class
    
    Args:
        meshes (Mesh3DPM): 3DPM onion result
        lcbs (list[Lcom]): Load combination
        strength (list[Lcom]): Strength result
    """
    meshes: Mesh3DPM = dataclass_field(default=Mesh3DPM(), description="3DPM onion result")
    lcbs: list[Lcom] = dataclass_field(default=[], description="Load combination")
    strength: list[Lcom] = dataclass_field(default=[], description="Strength result")

    class Config(MBaseModel.Config):
        title = "GSD 3DPM Result"

class SectionProperty(MBaseModel):
    """
    Section Property
    """
    Area: float = dataclass_field(default=0.0, description="Area")
    Asy: float = dataclass_field(default=0.0, description="Asy")
    Asz: float = dataclass_field(default=0.0, description="Asz")
    Ixx: float = dataclass_field(default=0.0, description="Ixx")
    Iyy: float = dataclass_field(default=0.0, description="Iyy")
    Izz: float = dataclass_field(default=0.0, description="Izz")
    Cy: float = dataclass_field(default=0.0, description="Cy")
    Cz: float = dataclass_field(default=0.0, description="Cz")
    Syp: float = dataclass_field(default=0.0, description="Syp")
    Sym: float = dataclass_field(default=0.0, description="Sym")
    Szp: float = dataclass_field(default=0.0, description="Szp")
    Szm: float = dataclass_field(default=0.0, description="Szm")
    Ipyy: float = dataclass_field(default=0.0, description="Ipyy")
    Ipzz: float = dataclass_field(default=0.0, description="Ipzz")
    Zy: float = dataclass_field(default=0.0, description="Zy")
    Zz: float = dataclass_field(default=0.0, description="Zz")
    ry: float = dataclass_field(default=0.0, description="ry")
    rz: float = dataclass_field(default=0.0, description="rz")

    class Config:
        title = "Section Property"
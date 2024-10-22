from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel
from moapy.steel_pre import SteelMomentModificationFactor
from moapy.enum_pre import enum_to_list, enAluminumMaterial_AA

class AluMaterial(MBaseModel):
    """
    Alu DB Material
    """
    code: str = dataclass_field(default='AA(A)', description="material code")
    matl: str = dataclass_field(default='2014-T6', description="material name", enum=enum_to_list(enAluminumMaterial_AA))
    product: str = dataclass_field(default='Extrusions', description="product type")

    class Config(MBaseModel.Config):
        title = "Alu DB Material"
        description = "Alu DB Material"

class AluMomentModificationFactor(SteelMomentModificationFactor):
    """
    Steel DB Moment Modification Factor
    """
    cb: float = dataclass_field(default=1.0, description="Cb Modification Factor")
    m: float = dataclass_field(default=1.0, description="m Modification Factor")

    class Config(MBaseModel.Config):
        title = "Aluminum Moment Modification Factor"
        description = "Aluminum Moment Modification Factor"
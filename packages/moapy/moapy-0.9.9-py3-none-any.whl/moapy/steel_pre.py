from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel
from moapy.enum_pre import enum_to_list, enConnectionType, enUnitLength, en_H_EN10365, enSteelMaterial_EN10025, en_H_AISC05_US
from moapy.data_pre import Length

# ==== Steel DB ====
class SteelLength(MBaseModel):
    """
    Steel DB Length
    """
    l_x: Length = dataclass_field(default=Length(value=3000.0, unit=enUnitLength.MM), title="Lx", description="Lx")
    l_y: Length = dataclass_field(default=Length(value=3000.0, unit=enUnitLength.MM), title="Ly", description="Ly")
    l_b: Length = dataclass_field(default=Length(value=3000.0, unit=enUnitLength.MM), title="Lb", description="Lateral-Torsional Buckling Length")

    class Config(MBaseModel.Config):
        title = "Steel Member Length"
        description = "Steel Member Length"

class SteelLength_EC(SteelLength):
    """
    Steel DB Length
    """
    l_t: Length = dataclass_field(default=Length(value=3000.0, unit=enUnitLength.MM), title="Lt", description="Torsional Buckling Length")

    class Config(MBaseModel.Config):
        title = "Steel Member Length"
        description = "Steel Member Length"

class SteelMomentModificationFactor(MBaseModel):
    """
    Steel DB Moment Modification Factor
    """
    c_mx: float = dataclass_field(default=1.0, title="Cmx", description="Cmx Modification Factor")
    c_my: float = dataclass_field(default=1.0, title="Cmy", description="Cmy Modification Factor")

    class Config(MBaseModel.Config):
        title = "Steel Moment Modification Factor"
        description = "Steel Moment Modification Factor"

class SteelMomentModificationFactor_EC(SteelMomentModificationFactor):
    """
    Steel DB Moment Modification Factor
    """
    c1: float = dataclass_field(default=1.0, description="ratio between the critical bending moment and the critical constant bending moment for a member with hinged supports")
    c_mlt: float = dataclass_field(default=1.0, description="equivalent uniform moment factor for LTB")

    class Config(MBaseModel.Config):
        title = "Steel Moment Modification Factor"
        description = "Steel Moment Modification Factor"

class SteelSection(MBaseModel):
    """
    Steel DB Section
    """
    shape: str = dataclass_field(default='H', description="Shape")
    name: str = dataclass_field(default='H 400x200x8/13', description="Section Name")

    class Config(MBaseModel.Config):
        title = "Steel DB Section"
        description = "Steel DB Section"

class SteelSection_AISC05_US(SteelSection):
    """
    Steel DB Section
    """
    shape: str = dataclass_field(default='H', description="Shape")
    name: str = dataclass_field(default='W40X362', description="Section Name", enum=enum_to_list(en_H_AISC05_US))

    class Config(MBaseModel.Config):
        title = "Steel DB Section"
        description = "Steel DB Section"

class SteelSection_EN10365(SteelSection):
    """
    Steel DB Section wit
    """
    shape: str = dataclass_field(default='H', description="Shape")
    name: str = dataclass_field(default='HD 260x54.1', description="Section Name", enum=enum_to_list(en_H_EN10365))

    class Config(MBaseModel.Config):
        title = "Steel DB Section"
        description = "Steel DB Section"

class SteelMaterial(MBaseModel):
    """
    Steel DB Material
    """
    code: str = dataclass_field(default='KS18(S)', description="Material Code")
    name: str = dataclass_field(default='SS275', description="Material Name")

    class Config(MBaseModel.Config):
        title = "Steel DB Material"
        description = "Steel DB Material"

class SteelMaterial_EC(SteelMaterial):
    """
    Steel DB Material
    """
    code: str = dataclass_field(default='EN10025', description="Material Code")
    name: str = dataclass_field(default='S275', description="Material Name", enum=enum_to_list(enSteelMaterial_EN10025))

    class Config(MBaseModel.Config):
        title = "Steel DB Material"
        description = "Steel DB Material"

class BoltMaterial(MBaseModel):
    """
    Bolt Material
    """
    name: str = dataclass_field(default='F10T', description="Bolt Material Name")

    class Config(MBaseModel.Config):
        title = "Bolt Material"
        description = "Bolt Material"

class SteelMember(MBaseModel):
    """
    Steel Member
    """
    sect: SteelSection = dataclass_field(default=SteelSection(), description="Section")
    matl: SteelMaterial = dataclass_field(default=SteelMaterial(), description="Material")

    class Config(MBaseModel.Config):
        title = "Steel Member"
        description = "Steel Member"

class SteelMember_EC(SteelMember):
    """
    Steel Member
    """
    sect: SteelSection_EN10365 = dataclass_field(default=SteelSection_EN10365(), description="Section")
    matl: SteelMaterial_EC = dataclass_field(default=SteelMaterial_EC(), description="Material")

    class Config(MBaseModel.Config):
        title = "Steel Member"
        description = "Steel Member"

class SteelConnectMember(MBaseModel):
    """
    Steel Connect Member
    """
    supporting: SteelMember = dataclass_field(default=SteelMember(), description="Supporting Member")
    supported: SteelMember = dataclass_field(default=SteelMember(), description="Supported Member")

    class Config(MBaseModel.Config):
        title = "Steel Connect Member"
        description = "Steel Connect Member"

class SteelConnectMember_EC(SteelConnectMember):
    """
    Steel Connect Member
    """
    supporting: SteelMember_EC = dataclass_field(default=SteelMember_EC(), description="Supporting Member")
    supported: SteelMember_EC = dataclass_field(default=SteelMember_EC(), description="Supported Member")

    class Config(MBaseModel.Config):
        title = "Steel Connect Member"
        description = "Steel Connect Member"

class SteelBolt(MBaseModel):
    """
    Steel Bolt
    """
    name: str = dataclass_field(default='M16', description="Bolt Size")
    matl: BoltMaterial = dataclass_field(default=BoltMaterial(), description="Material")

    class Config(MBaseModel.Config):
        title = "Steel Bolt"
        description = "Steel Bolt"

class ShearConnector(MBaseModel):
    """
    ShearConnector
    """
    bolt: SteelBolt = dataclass_field(default=SteelBolt(), description="Bolt")
    num: int = dataclass_field(default=1, description="Number of Bolts")
    space: Length = dataclass_field(default=Length(value=300.0, unit=enUnitLength.MM), description="spacing")
    length: Length = dataclass_field(default=Length(value=100.0, unit=enUnitLength.MM), description="length")

    class Config(MBaseModel.Config):
        title = "Shear Connector"
        description = "Shear Connector"

class Welding(MBaseModel):
    """
    Welding
    """
    matl: SteelMaterial = dataclass_field(default=SteelMaterial(), description="Material")
    length: Length = dataclass_field(default=Length(value=6.0, unit=enUnitLength.MM), description="Leg of Length")

    class Config(MBaseModel.Config):
        title = "Welding"
        description = "Welding"

class Welding_EC(Welding):
    """
    Welding
    """
    matl: SteelMaterial_EC = dataclass_field(default=SteelMaterial_EC(), description="Material")
    length: Length = dataclass_field(default=Length(value=6.0, unit=enUnitLength.MM), description="Leg of Length")

    class Config(MBaseModel.Config):
        title = "Welding"
        description = "Welding"

class SteelPlateMember(MBaseModel):
    """
    Steel Plate Member
    """
    matl: SteelMaterial = dataclass_field(default=SteelMaterial(), description="Material")
    bolt_num: int = dataclass_field(default=4, description="Number of Bolts")
    thk: Length = dataclass_field(default=Length(value=6.0, unit=enUnitLength.MM), description="Thickness")

    class Config(MBaseModel.Config):
        title = "Steel Plate Member"
        description = "Steel Plate Member"

class SteelPlateMember_EC(SteelPlateMember):
    """
    Steel Plate Member
    """
    matl: SteelMaterial_EC = dataclass_field(default=SteelMaterial_EC(), description="Material")
    bolt_num: int = dataclass_field(default=4, description="Number of Bolts")
    thk: Length = dataclass_field(default=Length(value=6.0, unit=enUnitLength.MM), description="Thickness")

    class Config(MBaseModel.Config):
        title = "Steel Plate Member"
        description = "Steel Plate Member"

class ConnectType(MBaseModel):
    """
    Connect Type class

    Args:
        type (str): Connection type
    """
    type: str = dataclass_field(default="Fin Plate - Beam to Beam", description="Connect type", enum=enum_to_list(enConnectionType))

    class Config(MBaseModel.Config):
        title = "Connection Type"

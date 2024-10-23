from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel
from moapy.enum_pre import enum_to_list, enConnectionType, enUnitLength, en_H_EN10365, enSteelMaterial_EN10025, en_H_AISC05_US, enBoltName, enBoltMaterialEC
from moapy.data_pre import Length

# ==== Steel DB ====
class SteelLength(MBaseModel):
    """
    Steel DB Length
    """
    l_x: Length = dataclass_field(default=Length(value=3000.0, unit=enUnitLength.MM), title="Lx", description="Unbraced length(x-direction)")
    l_y: Length = dataclass_field(default=Length(value=3000.0, unit=enUnitLength.MM), title="Ly", description="Unbraced length(y-direction)")
    l_b: Length = dataclass_field(default=Length(value=3000.0, unit=enUnitLength.MM), title="Lb", description="Lateral unbraced length")

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
    shape: str = dataclass_field(default='H', description="Shape of member section")
    name: str = dataclass_field(default='H 400x200x8/13', description="Section Name")

    class Config(MBaseModel.Config):
        title = "Steel DB Section"
        description = "Steel DB Section"

class SteelSection_AISC05_US(SteelSection):
    """
    Steel DB Section
    """
    shape: str = dataclass_field(default='H', description="Shape of member section")
    name: str = dataclass_field(default='W40X362', description="Section Name", enum=enum_to_list(en_H_AISC05_US))

    class Config(MBaseModel.Config):
        title = "Steel DB Section"
        description = "Steel DB Section"

class SteelSection_EN10365(SteelSection):
    """
    Steel DB Section wit
    """
    shape: str = dataclass_field(default='H', description="Shape of member section")
    name: str = dataclass_field(default='HD 260x54.1', description="use DB stored in EN10365", enum=enum_to_list(en_H_EN10365))

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
    code: str = dataclass_field(default='EN10025', description="Material code")
    name: str = dataclass_field(default='S275', description="Material of steel member", enum=enum_to_list(enSteelMaterial_EN10025))

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

class BoltMaterial_EC(MBaseModel):
    """
    Bolt Material
    """
    name: str = dataclass_field(default='4.8', description="Bolt Material Name", enum=enum_to_list(enBoltMaterialEC))

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
    sect: SteelSection_EN10365 = dataclass_field(default=SteelSection_EN10365(), description="Shape of section")
    matl: SteelMaterial_EC = dataclass_field(default=SteelMaterial_EC(), description="Material of steel member")

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
    supporting: SteelMember_EC = dataclass_field(default=SteelMember_EC(), title="supporting member", description="Supporting Member")
    supported: SteelMember_EC = dataclass_field(default=SteelMember_EC(), title="supported member", description="Supported Member")

    class Config(MBaseModel.Config):
        title = "Steel Connect Member"
        description = "Steel Connect Member"

class SteelBoltConnectionForce(MBaseModel):
    """
    Steel Bolt Connection Force
    """
    percent: float = dataclass_field(default=30.0, title="strength design(%)", description="Generally section of steel beam is determined by bending moment, typically shear is set 30% as default because there is no problem even if shear is assumed to about 30 % of member strength. If it is required to consider 100% of member strength, change the entered value.")

    class Config(MBaseModel.Config):
        title = "Steel Bolt Connection Force"
        description = "Steel Bolt Connection Force"

class SteelBolt(MBaseModel):
    """
    Steel Bolt
    """
    name: str = dataclass_field(default='M16', title="bolt name", description="Bolt size", enum=enum_to_list(enBoltName))
    matl: BoltMaterial = dataclass_field(default=BoltMaterial(), title="bolt material", description="Material of bolt")

    class Config(MBaseModel.Config):
        title = "Steel Bolt"
        description = "Steel Bolt"

class SteelBolt_EC(MBaseModel):
    """
    Steel Bolt
    """
    name: str = dataclass_field(default='M20', title="bolt name", description="Bolt size", enum=enum_to_list(enBoltName))
    matl: BoltMaterial_EC = dataclass_field(default=BoltMaterial_EC(), title="bolt material", description="Material of bolt")

    class Config(MBaseModel.Config):
        title = "Steel Bolt"
        description = "Steel Bolt"

class ShearConnector(MBaseModel):
    """
    ShearConnector
    """
    bolt: SteelBolt = dataclass_field(default=SteelBolt(), description="stud bolt")
    num: int = dataclass_field(default=1, description="stud column")
    space: Length = dataclass_field(default=Length(value=300.0, unit=enUnitLength.MM), description="stud spacing")
    length: Length = dataclass_field(default=Length(value=100.0, unit=enUnitLength.MM), description="stud length")

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

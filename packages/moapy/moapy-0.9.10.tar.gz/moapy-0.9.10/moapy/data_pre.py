from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel
from moapy.enum_pre import (
    enUnitThermalExpansion, enum_to_list, enDgnCode, enEccPu, enReportType,
    enUnitTemperature, enUnitLength, enUnitStress, enUnitForce, enUnitMoment, enUnitLoad, enUnitAngle)

# ==== Base ====
class Angle(MBaseModel):
    """
    Angle class
    """
    value: float = dataclass_field(default=0.0, description="Angle value")
    unit: enUnitAngle = dataclass_field(default=enUnitAngle.Degree)

class Load(MBaseModel):
    """
    Load class
    """
    value: float = dataclass_field(default=0.0, description="Load value")
    unit: enUnitLoad = dataclass_field(default=enUnitLoad.kN_m2)

class Temperature(MBaseModel):
    """
    Thermal
    """
    value: float = dataclass_field(default=0.0, description="Temperature")
    unit: enUnitTemperature = dataclass_field(default=enUnitTemperature.Celsius)

class Length(MBaseModel):
    """
    Length
    """
    value: float = dataclass_field(default=0.0, description="Length")
    unit: enUnitLength = dataclass_field(default=enUnitLength.MM)

class Force(MBaseModel):
    """
    Force
    """
    value: float = dataclass_field(default=0.0, description="Force")
    unit: enUnitForce = dataclass_field(default=enUnitForce.kN)

class Moment(MBaseModel):
    """
    Moment
    """
    value: float = dataclass_field(default=0.0, description="Moment")
    unit: enUnitMoment = dataclass_field(default=enUnitMoment.kNm)

class Stress(MBaseModel):
    """
    Stress
    """
    value: float = dataclass_field(default=0.0, description="Stress")
    unit: enUnitStress = dataclass_field(default=enUnitStress.MPa)

class ThermalExpansionCoeff(MBaseModel):
    """
    Thermal Expansion Coefficient
    """
    value: float = dataclass_field(default=1.0, description="Thermal Expansion Coefficient")
    unit: enUnitThermalExpansion = dataclass_field(default=enUnitThermalExpansion.PER_CELSIUS)

# ==== Length ====
class EffectiveLength(MBaseModel):
    """
    Effective Length class
    """
    kx: float = dataclass_field(default=1.0, description="Effect buckling length factor(x direction)")
    ky: float = dataclass_field(default=1.0, description="Effect buckling length factor(y direction)")

    class Config(MBaseModel.Config):
        title = "Effective Length"
        description = "Effective Length"

# ==== Forces ====
class UnitLoads(MBaseModel):
    """
    Unit Loads class
    """
    construction: Load = dataclass_field(default_factory=Load, title="construction load", description="Input construction load")
    live: Load = dataclass_field(default_factory=Load, title="live load", description="Input live load")
    finish: Load = dataclass_field(default_factory=Load, title="finish load", description="Input finishing load")

    class Config(MBaseModel.Config):
        title = "Unit Loads"

class MemberForce(MBaseModel):
    """Force class

    Args:
        Fz (float): Axial force
        Mx (float): Moment about x-axis
        My (float): Moment about y-axis
        Vx (float): Shear about x-axis
        Vy (float): Shear about y-axis
    """
    Fz: Force = dataclass_field(default_factory=Force, title="Fz", description="Axial force")
    Mx: Moment = dataclass_field(default_factory=Moment, title="Mx", description="Moment about x-axis")
    My: Moment = dataclass_field(default_factory=Moment, title="My", description="Moment about y-axis")
    Vx: Force = dataclass_field(default_factory=Force, title="Vx", description="Shear about x-axis")
    Vy: Force = dataclass_field(default_factory=Force, title="Vy", description="Shear about y-axis")

    class Config(MBaseModel.Config):
        title = "Member Force"
        description = "Member Force"

class AxialForceOpt(MBaseModel):
    """
    Moment Interaction Curve
    """
    Nx: Force = dataclass_field(default_factory=Force, title="Nx", description="Axial Force")

    class Config:
        title = "Axial Force Option"

class DesignCode(MBaseModel):
    """Design Code class

    Args:
        design_code (str): Design code
        sub_code (str): Sub code
    """    
    design_code: str = dataclass_field(default="ACI 318-19", max_length=30)
    sub_code: str = dataclass_field(default="SI")

    class Config(MBaseModel.Config):
        title = "GSD Design Code"

class DgnCode(MBaseModel):
    """
    DgnCode
    """
    name: str = dataclass_field(default="", description="DgnCode")

    class Config:
        title = "DgnCode"

# ==== Lcoms ====
class Lcom(MBaseModel):
    """
    Lcom class

    Args:
        name (str): load combination name
        f (Force): load combination force
    """
    name: str = dataclass_field(default="lcom", description="load combination name")
    f: MemberForce = dataclass_field(default_factory=MemberForce, title="force", description="load combination force")

    class Config(MBaseModel.Config):
        title = "Lcom Result"

class Lcoms(MBaseModel):
    """
    Lcoms class

    Args:
        lcoms (list[Lcom]): load combination result
    """
    lcoms: list[Lcom] = dataclass_field(default=[Lcom(name="uls1", f=MemberForce(Fz=Force(value=100.0, unit=enUnitForce.kN),
                                                                                 Mx=Moment(value=10.0, unit=enUnitMoment.kNm),
                                                                                 My=Moment(value=50.0, unit=enUnitMoment.kNm)))], description="load combination result")

    class Config(MBaseModel.Config):
        title = "Strength Result"

class AngleOpt(MBaseModel):
    """
    Angle Option
    """
    theta: Angle = dataclass_field(default_factory=Angle, title="angle", description="theta")

    class Config:
        title = "Theta Option"

class ElasticModulusOpt(MBaseModel):
    """
    Elastic Modulus Option
    """
    E: Stress = dataclass_field(default=Stress(value=200.0, unit=enUnitStress.MPa), title="E", description="Elastic Modulus")

    class Config:
        title = "Elastic Modulus Option"

class Unit(MBaseModel):
    """
    GSD global unit class
    
    Args:
        force (str): Force unit
        length (str): Length unit
        section_dimension (str): Section dimension unit
        pressure (str): Pressure unit
        strain (str): Strain unit
    """
    force: str = dataclass_field(
        default="kN", description="Force unit")
    length: str = dataclass_field(
        default="m", description="Length unit")
    section_dimension: str = dataclass_field(
        default="mm", description="Section dimension unit")
    pressure: str = dataclass_field(
        default="MPa", description="Pressure unit")
    strain: str = dataclass_field(
        default="%", description="Strain unit")

    class Config(MBaseModel.Config):
        title = "GSD Unit"

# ==== Stress Strain Curve ====
class Stress_Strain_Component(MBaseModel):
    """Stress Strain Component class

    Args:
        stress (float): Stress
        strain (float): Strain
    """
    stress: float = dataclass_field(default=0.0, description="Stress")
    strain: float = dataclass_field(default=0.0, description="Strain")

    class Config(MBaseModel.Config):
        title = "Stress Strain Component"

# ==== Geometry ====
class Point(MBaseModel):
    """
    Point class

    Args:
        x (float): x-coordinate
        y (float): y-coordinate
    """
    x: Length
    y: Length

    class Config(MBaseModel.Config):
        title = "Point"

class Points(MBaseModel):
    """
    GSD Points class

    Args:
        points (list[Point]): Points
    """
    points: list[Point] = dataclass_field(default=[Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)),
                                                   Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)),
                                                   Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM)),
                                                   Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM))], description="Points")

    class Config(MBaseModel.Config):
        title = "GSD Points"

class OuterPolygon(MBaseModel):
    """
    GSD Outer Polygon class

    Args:
        points (list[Point]): Points
    """
    points: list[Point] = dataclass_field(default=[Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)),
                                                   Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)),
                                                   Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM)),
                                                   Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM))], description="Outer Polygon")

    class Config(MBaseModel.Config):
        title = "GSD Outer Polygon"

class InnerPolygon(MBaseModel):
    """
    GSD Inner Polygon class

    Args:
        points (list[Point]): Points
    """
    points: list[Point] = dataclass_field(default=[Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)), 
                                                   Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)), 
                                                   Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM)), 
                                                   Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM))], description="Inner Polygon")

    class Config(MBaseModel.Config):
        title = "GSD Inner Polygon"

class Lcb(MBaseModel):
    """
    GSD load combination class
    
    Args:
        uls (Lcoms): uls load combination
    """
    uls: Lcoms = dataclass_field(default=Lcoms(), description="uls load combination")

    class Config(MBaseModel.Config):
        title = "GSD Load Combination"

# ==== options ====
class PMOptions(MBaseModel):
    """
    GSD options class
    
    Args:
        dgncode (str): Design code
        by_ecc_pu (str): ecc
    """
    dgncode: str = dataclass_field(default=enDgnCode.Eurocode2_04, description="Design code", enum=enum_to_list(enDgnCode))
    by_ecc_pu: str = dataclass_field(default="ecc", description="ecc or P-U", enum=enum_to_list(enEccPu))

    class Config(MBaseModel.Config):
        title = "GSD Options"

class ReportType(MBaseModel):
    """
    Report Type class
    
    Args:
        report_type (str): Report type
    """
    type: str = dataclass_field(default="markdown", description="Report type", enum=enum_to_list(enReportType))

    class Config(MBaseModel.Config):
        title = "Report Type"
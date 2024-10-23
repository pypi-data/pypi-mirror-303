from typing import Optional
from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel
from moapy.data_pre import Point, Stress_Strain_Component, Length, enUnitLength
# ==== Concrete Material ====
class ConcreteGrade(MBaseModel):
    """
    GSD concrete class

    Args:
        design_code (str): Design code
        grade (str): Grade of the concrete
    """
    design_code: str = dataclass_field(
        default="ACI318M-19", description="Design code")
    grade: str = dataclass_field(
        default="C12", description="Grade of the concrete")

    class Config(MBaseModel.Config):
        title = "GSD Concrete Grade"

class Concrete_General_Properties(MBaseModel):
    """
    GSD concrete general properties for calculation
    
    Args:
        strength (int): Grade of the concrete
        elastic_modulus (float): Elastic modulus of the concrete
        density (float): Density of the concrete
        thermal_expansion_coefficient (float): Thermal expansion coefficient of the concrete
        poisson_ratio (float): Poisson ratio of the concrete
    """
    strength: int = dataclass_field(
        gt=0, default=12, description="Grade of the concrete")
    elastic_modulus: float = dataclass_field(
        gt=0, default=30000, description="Elastic modulus of the concrete")
    density: float = dataclass_field(
        gt=0, default=2400, description="Density of the concrete")
    thermal_expansion_coefficient: float = dataclass_field(
        gt=0, default=0.00001, description="Thermal expansion coefficient of the concrete")
    poisson_ratio: float = dataclass_field(
        gt=0, default=0.2, description="Poisson ratio of the concrete")

    class Config(MBaseModel.Config):
        title = "GSD Concrete General Properties"

class Concrete_Stress_ULS_Options_ACI(MBaseModel):
    """
    GSD concrete stress options for ULS
    
    Args:
        material_model (str): Material model for ULS
        factor_b1 (float): Plastic strain limit for ULS
        compressive_failure_strain (float): Failure strain limit for ULS
    """
    material_model: str = dataclass_field(
        default="Rectangle", description="Material model for ULS")
    factor_b1: float = dataclass_field(
        default=0.85, description="Plastic strain limit for ULS")
    compressive_failure_strain: float = dataclass_field(
        default=0.003, description="Failure strain limit for ULS")

    class Config(MBaseModel.Config):
        title = "GSD Concrete Stress Options for ULS"

class Concrete_Stress_ULS_Options_Eurocode(MBaseModel):
    """
    GSD concrete stress options for ULS
    
    Args:
        material_model (str): Material model for ULS
        partial_factor_case (float): Partial factor case for ULS
        partial_factor (float): Partial factor for ULS
        compressive_failure_strain (float): Failure strain limit for ULS
    """
    material_model: str = dataclass_field(
        default="Rectangle", description="Material model for ULS")
    partial_factor_case: float = dataclass_field(
        default=1.0, description="Partial factor case for ULS")
    partial_factor: float = dataclass_field(
        default=1.5, description="Partial factor for ULS")
    compressive_failure_strain: float = dataclass_field(
        default=0.003, description="Failure strain limit for ULS")

    class Config(MBaseModel.Config):
        title = "GSD Concrete Stress Options for ULS"

class Concrete_SLS_Options(MBaseModel):
    """
    GSD concrete stress options for SLS
    
    Args:
        material_model (str): Material model for SLS
        plastic_strain_limit (float): Plastic strain limit for SLS
        failure_compression_limit (float): Failure compression limit for SLS
        material_model_tension (str): Material model for SLS tension
        failure_tension_limit (float): Failure tension limit for SLS
    """
    material_model: str = dataclass_field(
        default="Linear", description="Material model for SLS")
    plastic_strain_limit: float = dataclass_field(
        default=0.002, description="Plastic strain limit for SLS")
    failure_compression_limit: float = dataclass_field(
        default=0.003, description="Failure compression limit for SLS")
    material_model_tension: str = dataclass_field(
        default="interpolated", description="Material model for SLS tension")
    failure_tension_limit: float = dataclass_field(
        default=0.003, description="Failure tension limit for SLS")

    class Config(MBaseModel.Config):
        title = "GSD Concrete Stress Options for SLS"

# ==== Rebar & Tendon Materials ====
class RebarGrade(MBaseModel):
    """
    GSD rebar grade class
    
    Args:
        design_code (str): Design code
        grade (str): Grade of the rebar
    """
    design_code: str = dataclass_field(
        default="ACI318M-19", description="Design code")
    grade: str = dataclass_field(
        default="Grade 420", description="Grade of the rebar")

    class Config(MBaseModel.Config):
        title = "GSD Rebar Grade"

class TendonGrade(MBaseModel):
    """
    GSD Tendon grade class
    
    Args:
        design_code (str): Design code
        grade (str): Grade of the tendon
    """
    design_code: str = dataclass_field(
        default="ACI318M-19", description="Design code")
    grade: str = dataclass_field(default="Grade 420", description="Grade of the tendon")

    class Config(MBaseModel.Config):
        title = "GSD Tendon Grade"

class RebarProp(MBaseModel):
    """
    GSD rebar prop
    
    Args:
        area (float): Area of the rebar
        material (RebarGrade): Material of the rebar
    """
    area: float = dataclass_field(default=287.0, description="Area of the rebar")
    material: RebarGrade = dataclass_field(default=RebarGrade(), description="Material of the rebar")

    class Config(MBaseModel.Config):
        title = "GSD Rebar Properties"

class TendonProp(MBaseModel):
    """
    GSD Tendon prop
    
    Args:
        area (float): Area of the tendon
        material (TendonGrade): Material of the tendon
        prestress (float): Prestress of the tendon
    """
    area: float = dataclass_field(default=287.0, description="Area of the tendon")
    material: TendonGrade = dataclass_field(default=TendonGrade(), description="Material of the tendon")
    prestress: float = dataclass_field(default=0.0, description="Prestress of the tendon")

    class Config(MBaseModel.Config):
        title = "GSD Tendon Properties"

class Rebar_General_Properties(MBaseModel):
    """
    GSD rebar general properties for calculation
    
    Args:
        strength (int): Grade of the rebar
        elastic_modulus (float): Elastic modulus of the rebar
        density (float): Density of the rebar
        thermal_expansion_coefficient (float): Thermal expansion coefficient of the rebar
        poisson_ratio (float): Poisson ratio of the rebar
    """
    strength: int = dataclass_field(
        default=420, description="Grade of the rebar")
    elastic_modulus: float = dataclass_field(
        default=200000, description="Elastic modulus of the rebar")
    density: float = dataclass_field(
        default=7850, description="Density of the rebar")
    thermal_expansion_coefficient: float = dataclass_field(
        default=0.00001, description="Thermal expansion coefficient of the rebar")
    poisson_ratio: float = dataclass_field(
        default=0.3, description="Poisson ratio of the rebar")

    class Config(MBaseModel.Config):
        title = "GSD Rebar General Properties"

class Rebar_Stress_ULS_Options_ACI(MBaseModel):
    """
    GSD rebar stress options for ULS
    
    Args:
        material_model (str): Material model for ULS
        failure_strain (float): Failure strain limit for ULS
    """
    material_model: str = dataclass_field(
        default="Elastic-Plastic", description="Material model for ULS")
    failure_strain: float = dataclass_field(
        default=0.7, description="Failure strain limit for ULS")

    class Config(MBaseModel.Config):
        title = "GSD Rebar Stress Options for ULS"

class Rebar_Stress_SLS_Options(MBaseModel):
    """
    GSD rebar stress options for SLS
    
    Args:
        material_model (str): Material model for SLS
        failure_strain (float): Failure strain limit for SLS
    """
    material_model: str = dataclass_field(
        default="Elastic-Plastic", description="Material model for SLS")
    failure_strain: float = dataclass_field(
        default=0.7, metadata={"default" : 0.7, "description": "Failure strain limit for SLS"})

    class Config(MBaseModel.Config):
        title = "GSD Rebar Stress Options for SLS"

class MaterialRebar(MBaseModel):
    """
    GSD rebar class
    
    Args:
        grade (RebarGrade): Grade of the rebar
        curve_uls (list[Stress_Strain_Component]): Stress strain curve for ULS
        curve_sls (list[Stress_Strain_Component]): Stress strain curve for SLS
    """
    grade: RebarGrade = dataclass_field(
        default=RebarGrade(), description="Grade of the rebar")
    curve_uls: list[Stress_Strain_Component] = dataclass_field(default=[Stress_Strain_Component(strain=0.0, stress=0.0), Stress_Strain_Component(strain=0.0025, stress=500.0), Stress_Strain_Component(strain=0.05, stress=500.0)], description="Stress strain curve")
    curve_sls: list[Stress_Strain_Component] = dataclass_field(default=[Stress_Strain_Component(strain=0.0, stress=0.0), Stress_Strain_Component(strain=0.0025, stress=500.0), Stress_Strain_Component(strain=0.05, stress=500.0)], description="Stress strain curve")

    class Config(MBaseModel.Config):
        title = "GSD Material Rebar"

class MaterialTendon(MBaseModel):
    """
    GSD tendon class
    
    Args:
        grade (TendonGrade): Grade of the tendon
        curve_uls (list[Stress_Strain_Component]): Stress strain curve for ULS
        curve_sls (list[Stress_Strain_Component]): Stress strain curve for SLS
    """
    grade: TendonGrade = dataclass_field(default=TendonGrade(), description="Grade of the tendon")
    curve_uls: list[Stress_Strain_Component] = dataclass_field(default=[Stress_Strain_Component(strain=0.0, stress=0.0), Stress_Strain_Component(strain=0.00725, stress=1450.0), Stress_Strain_Component(strain=0.05, stress=1750.0)], description="Stress strain curve")
    curve_sls: list[Stress_Strain_Component] = dataclass_field(default=[Stress_Strain_Component(strain=0.0, stress=0.0), Stress_Strain_Component(strain=0.00725, stress=1450.0), Stress_Strain_Component(strain=0.05, stress=1750.0)], description="Stress strain curve")

    class Config(MBaseModel.Config):
        title = "GSD Material Tendon"

class MaterialConcrete(MBaseModel):
    """
    GSD material for Concrete class
    
    Args:
        grade (ConcreteGrade): Grade of the concrete
        curve_uls (list[Stress_Strain_Component]): Stress strain curve concrete ULS
        curve_sls (list[Stress_Strain_Component]): Stress strain curve
    """
    grade: ConcreteGrade = dataclass_field(
        default=ConcreteGrade(), description="Grade of the concrete")
    curve_uls: list[Stress_Strain_Component] = dataclass_field(default=[Stress_Strain_Component(strain=0.0, stress=0.0), Stress_Strain_Component(strain=0.0006, stress=0.0), Stress_Strain_Component(strain=0.0006, stress=34.0), Stress_Strain_Component(strain=0.003, stress=34.0)], description="Stress strain curve concrete ULS")
    curve_sls: list[Stress_Strain_Component] = dataclass_field(default=[Stress_Strain_Component(strain=0.0, stress=0.0), Stress_Strain_Component(strain=0.001, stress=32.8)], description="Stress strain curve")

    class Config(MBaseModel.Config):
        title = "GSD Material Concrete"

class Material(MBaseModel):
    """
    GSD concrete class

    Args:
        concrete (MaterialConcrete): Concrete properties
        rebar (MaterialRebar): Rebar properties
        tendon (MaterialTendon): Tendon properties
    """
    concrete: MaterialConcrete = dataclass_field(default=MaterialConcrete(), description="Concrete properties")
    rebar: Optional[MaterialRebar] = dataclass_field(default=MaterialRebar(), description="Rebar properties")
    tendon: Optional[MaterialTendon] = dataclass_field(default=MaterialTendon(), description="Tendon properties")

    def __post_init__(self):
        if self.rebar is None and self.tendon is None:
            raise ValueError("Either rebar or tendon must be provided.")

    class Config(MBaseModel.Config):
        title = "GSD Material"

class ConcreteGeometry(MBaseModel):
    """
    GSD concrete geometry class
    
    Args:
        material (ConcreteGrade): Material of the concrete
        outerPolygon (list[Point]): Outer polygon of the concrete
        innerPolygon (list[Point]): Inner polygon of the concrete
    """
    material: ConcreteGrade = dataclass_field(default=ConcreteGrade(), description="Material of the concrete")
    outerPolygon: list[Point] = dataclass_field(default=[Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)), Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=0.0, unit=enUnitLength.MM)), 
                                                         Point(x=Length(value=400.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM)), Point(x=Length(value=0.0, unit=enUnitLength.MM), y=Length(value=600.0, unit=enUnitLength.MM))], description="Outer polygon of the concrete")
    innerPolygon: list[Point] = dataclass_field(default=[Point(x=Length(value=80.0, unit=enUnitLength.MM), y=Length(value=80.0, unit=enUnitLength.MM)), Point(x=Length(value=320.0, unit=enUnitLength.MM), y=Length(value=80.0, unit=enUnitLength.MM)),
                                                         Point(x=Length(value=320.0, unit=enUnitLength.MM), y=Length(value=520.0, unit=enUnitLength.MM)), Point(x=Length(value=80.0, unit=enUnitLength.MM), y=Length(value=520.0, unit=enUnitLength.MM))], description="Inner polygon of the concrete")

    class Config(MBaseModel.Config):
        title = "GSD Concrete Geometry"

class RebarGeometry(MBaseModel):
    """
    GSD rebar geometry class

    Args:
        prop (RebarProp): properties of the rebar
        points (list[Point]): Rebar Points
    """
    prop: RebarProp = dataclass_field(default=RebarProp(), description="properties of the rebar")
    points: list[Point] = dataclass_field(default=[Point(x=Length(value=40.0, unit=enUnitLength.MM), y=Length(value=40.0, unit=enUnitLength.MM)), Point(x=Length(value=360.0, unit=enUnitLength.MM), y=Length(value=40.0, unit=enUnitLength.MM)),
                                                   Point(x=Length(value=360.0, unit=enUnitLength.MM), y=Length(value=560.0, unit=enUnitLength.MM)), Point(x=Length(value=40.0, unit=enUnitLength.MM), y=Length(value=560.0, unit=enUnitLength.MM))], description="Rebar Points")

    class Config(MBaseModel.Config):
        title = "GSD Rebar Geometry"

class TendonGeometry(MBaseModel):
    """
    GSD tendon geometry class
    
    Args:
        prop (TendonProp): properties of the tendon
        points (list[Point]): Tendon Points
    """
    prop: TendonProp = dataclass_field(default=TendonProp(), description="properties of the tendon")
    points: list[Point] = dataclass_field(default=[], description="Tendon Points")

    class Config(MBaseModel.Config):
        title = "GSD Tendon Geometry"

class Geometry(MBaseModel):
    """
    GSD geometry class
    
    Args:
        concrete (ConcreteGeometry): Concrete geometry
        rebar (RebarGeometry): Rebar geometry
        tendon (TendonGeometry): Tendon geometry
    """
    concrete: ConcreteGeometry = dataclass_field(default=ConcreteGeometry(), description="Concrete geometry")
    rebar: Optional[RebarGeometry] = dataclass_field(default=RebarGeometry(), description="Rebar geometry")
    tendon: Optional[TendonGeometry] = dataclass_field(default=TendonGeometry(), description="Tendon geometry")

    class Config(MBaseModel.Config):
        title = "GSD Geometry"

class SlabSection(MBaseModel):
    """
    Slab
    """
    thickness: Length = dataclass_field(default=Length(value=150.0, unit=enUnitLength.MM), title="Thick", description="slab thickness")

    class Config(MBaseModel.Config):
        title = "Slab"
        description = "Slab"

class GirderLength(MBaseModel):
    """
    Girder Length
    """
    span: Length = dataclass_field(default=Length(value=10.0, unit=enUnitLength.M), title="span length", description="Span Length")
    spacing: Length = dataclass_field(default=Length(value=3.0, unit=enUnitLength.M), title="spacing", description="Spacing")

    class Config(MBaseModel.Config):
        title = "Girder Length"
        description = "Girder Length"

class NeutralAxisDepth(MBaseModel):
    """
    Neutral Axis Depth
    """
    depth: Length = dataclass_field(default=Length(value=0.0, unit=enUnitLength.MM), title="Neutral Axis Depth", description="Neutral Axis Depth")

    class Config(MBaseModel.Config):
        title = "Neutral Axis Depth"
        description = "Neutral Axis Depth"
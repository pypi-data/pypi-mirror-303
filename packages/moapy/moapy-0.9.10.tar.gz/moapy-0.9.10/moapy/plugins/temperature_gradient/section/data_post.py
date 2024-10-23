from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel
from moapy.data_pre import (
    Point,
    Length,
    Stress,
    Temperature,
)


class ResultThermal(MBaseModel):
    """
    Result Thermal
    """

    y: list[Length] = dataclass_field(default_factory=list, description="Y")
    z: list[Length] = dataclass_field(default_factory=list, description="Z")
    temp: list[Temperature] = dataclass_field(
        default_factory=list, description="Temperature"
    )
    stress: list[Stress] = dataclass_field(default_factory=list, description="Stress")


class ResultNonlinearTemperatureEffect(MBaseModel):
    """
    Result Nonlinear Temperature Effect
    """
    height: Length = dataclass_field(default_factory=Length, description="Height")
    outer: list[Point] = dataclass_field(
        default_factory=list[Point], description="Outer polygon"
    )
    inner: list[list[Point]] = dataclass_field(
        default_factory=list[Point], description="Inner polygon"
    )
    heating: ResultThermal = dataclass_field(
        default_factory=ResultThermal, description="Heating"
    )
    cooling: ResultThermal = dataclass_field(
        default_factory=ResultThermal, description="Cooling"
    )
    temp_heating: list[Point] = dataclass_field(
        default_factory=list[Point], description="Temperature Heating"
    )
    temp_cooling: list[Point] = dataclass_field(
        default_factory=list[Point], description="Temperature Cooling"
    )

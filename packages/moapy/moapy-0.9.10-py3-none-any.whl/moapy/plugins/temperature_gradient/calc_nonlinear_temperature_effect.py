"""Calculates Temporature Gradient from Section"""

from moapy.auto_convert import auto_schema
from moapy.plugins.temperature_gradient.section.ctg_calc import (
    calc_section_temperature_gradient,
)
from moapy.plugins.temperature_gradient.section.data_input import (
    NonlinearTemperatureInput,
)
from moapy.plugins.temperature_gradient.section.data_post import (
    ResultNonlinearTemperatureEffect,
)
from moapy.plugins.temperature_gradient.section.data_pre import (
    CompositeSection,
)


@auto_schema(
    title="Calculate Temperature Gradient",
    description="Calculate Temperature Gradient from Section",
)
def calc_nonlinear_temperature_effect(
    nonlinear_temperature_input: NonlinearTemperatureInput,
) -> ResultNonlinearTemperatureEffect:
    section = nonlinear_temperature_input.section_input.section
    surface = nonlinear_temperature_input.surfacing_input

    geometry = section.calc_section_coordinate()
    section_group = section.get_group()

    if isinstance(section, CompositeSection):
        girder_material = section.girder_section.material
        slab_material = section.slab_section.material
    else:
        girder_material = section.material
        slab_material = section.material

    match surface.surfacing_type:
        case "unsurfaced" | "waterproofed":
            surface_thickness = surface.surfacing_type
        case "surfacing":
            surface_thickness = surface.surfacing_thickness.value
        case _:
            raise ValueError(f"Invalid surfacing_type: {surface.surfacing_type}")

    return calc_section_temperature_gradient(
        outer=geometry.outer,
        inner=geometry.inner,
        slab=geometry.comp,
        g_thermal=girder_material.thermal_expansion.value,
        s_thermal=slab_material.thermal_expansion.value,
        g_elastic=girder_material.elastic_modulus.value,
        s_elastic=slab_material.elastic_modulus.value,
        group=section_group,
        surf_thick=surface_thickness,
    )

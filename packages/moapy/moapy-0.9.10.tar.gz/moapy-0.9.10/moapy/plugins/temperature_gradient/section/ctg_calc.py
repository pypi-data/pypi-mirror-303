from moapy.data_pre import Length, Point, Stress, Temperature
from moapy.enum_pre import enUnitLength, enUnitStress, enUnitTemperature
from moapy.plugins.temperature_gradient.calc_eurocode import (
    interpolate_temperature,
    section_calculator,
    section_dimension,
    self_equilibrating_stress,
)
from moapy.plugins.temperature_gradient.section.data_post import (
    ResultNonlinearTemperatureEffect,
    ResultThermal,
)
# from moapy.plugins.temperature_gradient.section_properties import section_calculator


def calc_section_temperature_gradient(
    outer, inner, slab, g_thermal, s_thermal, g_elastic, s_elastic, group, surf_thick
):
    # Calculate the section properties
    sec_prop = section_calculator(outer, inner, slab, g_elastic, s_elastic)
    sec_dim = section_dimension(outer, inner, slab)

    slab_depth = sec_dim["slab_thick"]
    sect_height = sec_dim["height"]

    # print section calculation results
    # preprocess_result_print(outer, inner, slab, sec_prop, sec_dim)

    # Calculate the temperature distribution
    inf_point, inf_temp_h, inf_temp_c, point_h, temp_h, point_c, temp_c = (
        interpolate_temperature(group, sect_height, surf_thick, slab_depth)
    )

    # print temperature distribution results
    # plot_graphs("Steel Box", outer, inner, slab, point_h, temp_h, point_c, temp_c)

    # Calculate the self equilibrating stress
    self_eq_stress = self_equilibrating_stress(
        outer,
        inner,
        slab,
        g_thermal,
        s_thermal,
        g_elastic,
        s_elastic,
        sec_prop,
        sec_dim,
        inf_point,
        inf_temp_h,
        inf_temp_c,
    )
    out_points = [
        Point(
            x=Length(value=xv, unit=enUnitLength.MM),
            y=Length(value=yv, unit=enUnitLength.MM),
        )
        for xv, yv in zip(outer[0], outer[1])
    ]
    inner_points = [
        [
            Point(
                x=Length(value=xv, unit=enUnitLength.MM),
                y=Length(value=yv, unit=enUnitLength.MM),
            )
            for xv, yv in zip(inner[0], inner[1])
        ]
    ]
    heating = ResultThermal(
        y=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[0][0]["y"]
        ),
        z=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[0][0]["z"]
        ),
        temp=list(
            Temperature(value=xv, unit=enUnitTemperature.Celsius)
            for xv in self_eq_stress[0][0]["t"]
        ),
        stress=list(
            Stress(value=xv, unit=enUnitStress.MPa) for xv in self_eq_stress[0][0]["s"]
        ),
    )
    cooling = ResultThermal(
        y=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[1][0]["y"]
        ),
        z=list(
            Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[1][0]["z"]
        ),
        temp=list(
            Temperature(value=xv, unit=enUnitTemperature.Celsius)
            for xv in self_eq_stress[1][0]["t"]
        ),
        stress=list(
            Stress(value=xv, unit=enUnitStress.MPa) for xv in self_eq_stress[1][0]["s"]
        ),
    )
    return ResultNonlinearTemperatureEffect(
        height=Length(value=sect_height, unit=enUnitLength.MM),
        outer=out_points,
        inner=inner_points,
        heating=heating,
        cooling=cooling,
        temp_heating=[
            Point(
                x=Length(value=xv, unit=enUnitLength.MM),
                y=Length(value=yv, unit=enUnitLength.MM),
            )
            for xv, yv in zip(temp_h, point_h)
        ],
        temp_cooling=[
            Point(
                x=Length(value=xv, unit=enUnitLength.MM),
                y=Length(value=yv, unit=enUnitLength.MM),
            )
            for xv, yv in zip(temp_c, point_c)
        ],
    )

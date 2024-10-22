from moapy.data_pre import Length
from moapy.plugins.temperature_gradient.section.ctg_calc import (
    calc_section_temperature_gradient,
)
from moapy.plugins.temperature_gradient.section.data_post import (
    ResultNonlinearTemperatureEffect,
)
from moapy.plugins.temperature_gradient.section.data_pre import (
    CompositeBoxGirderSection,
    SectionMaterial,
    SlabSection,
    SlabSectionShape,
    SteelBoxGirderSection,
    SteelBoxGirderSectionShape,
    SteelIGirderSection,
    SteelIGirderSectionShape,
)


BASE_SECTION_RESULT_DIR = "./tests/calc_temperature_gradient/data/"


def get_result(file_path):
    # if file_path is relative path, convert to absolute path
    if not file_path.startswith("/"):
        file_path = BASE_SECTION_RESULT_DIR + file_path

    with open(file_path, "r") as f:
        return ResultNonlinearTemperatureEffect.model_validate_json(f.read())


def test_calc_temperature_gradient_SteelBoxGirderSection():
    section = SteelBoxGirderSection(
        shape=SteelBoxGirderSectionShape(),
        material=SectionMaterial(thermal_expansion=12e-6, elastic_modulus=210000),
    )
    surfacing_thickness = 30

    geometry = section.calc_section_coordinate()
    section_group = section.get_group()
    girder_material = section.material

    res = calc_section_temperature_gradient(
        outer=geometry.outer,
        inner=geometry.inner,
        slab=geometry.comp,
        g_thermal=girder_material.thermal_expansion,
        s_thermal=girder_material.thermal_expansion,
        g_elastic=girder_material.elastic_modulus,
        s_elastic=girder_material.elastic_modulus,
        group=section_group,
        surf_thick=surfacing_thickness,
    )

    expected = get_result("steel_box_example.json")

    assert res == expected


def test_calc_temperature_gradient_SteelIGirderSection():
    section = SteelIGirderSection(
        shape=SteelIGirderSectionShape(
            top=Length(value=0, unit="mm"),
            bot=Length(value=-50, unit="mm"),
            b1=Length(value=200, unit="mm"),
            b2=Length(value=200, unit="mm"),
            b3=Length(value=250, unit="mm"),
            b4=Length(value=250, unit="mm"),
            h=Length(value=700, unit="mm"),
            t1=Length(value=25, unit="mm"),
            t2=Length(value=30, unit="mm"),
            tw=Length(value=28, unit="mm"),
        ),
        material=SectionMaterial(thermal_expansion=12e-6, elastic_modulus=210000),
    )
    surfacing_thickness = 30

    geometry = section.calc_section_coordinate()
    section_group = section.get_group()
    girder_material = section.material

    res = calc_section_temperature_gradient(
        outer=geometry.outer,
        inner=geometry.inner,
        slab=geometry.comp,
        g_thermal=girder_material.thermal_expansion,
        s_thermal=girder_material.thermal_expansion,
        g_elastic=girder_material.elastic_modulus,
        s_elastic=girder_material.elastic_modulus,
        group=section_group,
        surf_thick=surfacing_thickness,
    )

    expected = get_result("steel_I_example.json")

    assert res == expected


def test_calc_temperature_gradient_CompositeSteelBoxSection():
    # refSize = ["Sg", "Top", "Bot"]
    # refSize = [0, 300, 580]
    # slab = ["Bc", "tc", "Hh"]
    # slab = [1800, 150, 0]
    # vSize = ["B1", "B2", "B3", "B4","B5", "B6", "H", "t1", "t2", "tw1", "tw2"]
    # vSize = [200, 800, 200, 120, 400, 120, 900, 24, 24, 26, 26]

    # girder_section = SteelBoxGirderSection(
    #     shape=SteelBoxGirderSectionShape(
    #         top=Length(value=300, unit="mm"),
    #         bot=Length(value=580, unit="mm"),
    #         b1=Length(value=200, unit="mm"),
    #         b2=Length(value=800, unit="mm"),
    #         b3=Length(value=200, unit="mm"),
    #         b4=Length(value=120, unit="mm"),
    #         b5=Length(value=400, unit="mm"),
    #         b6=Length(value=120, unit="mm"),
    #         h=Length(value=900, unit="mm"),
    #         t1=Length(value=24, unit="mm"),
    #         t2=Length(value=24, unit="mm"),
    #         tw1=Length(value=26, unit="mm"),
    #         tw2=Length(value=26, unit="mm"),
    #     ),
    #     material=SectionMaterial(thermal_expansion=12e-6, elastic_modulus=210000),
    # )
    # slab_section = SlabSection(
    #     shape=SlabSectionShape(
    #         sg=Length(value=0, unit="mm"),
    #         bc=Length(value=1800, unit="mm"),
    #         tc=Length(value=150, unit="mm"),
    #         hh=Length(value=0, unit="mm"),
    #     ),
    #     material=SectionMaterial(thermal_expansion=12e-6, elastic_modulus=210000),
    # )
    # section = CompositeBoxGirderSection(
    #     girderSection=girder_section,
    #     slabSection=slab_section,
    # )

    # surfacing_thickness = 30

    # geometry = section.calc_section_coordinate()
    # section_group = section.get_group()
    # girder_material = section.girderSection.material
    # slab_material = section.slabSection.material

    # res = calc_section_temperature_gradient(
    #     outer=geometry.outer,
    #     inner=geometry.inner,
    #     slab=geometry.comp,
    #     g_thermal=girder_material.thermal_expansion,
    #     s_thermal=slab_material.thermal_expansion,
    #     g_elastic=girder_material.elastic_modulus,
    #     s_elastic=slab_material.elastic_modulus,
    #     group=section_group,
    #     surf_thick=surfacing_thickness,
    # )

    # expected = get_result("composite_steel_box_example.json")

    pass


def test_calc_temperature_gradient_CompositeIGirderSection():
    pass


def test_calc_temperature_gradient_CompositeTubGirderSection():
    pass


def test_calc_temperature_gradient_PSC1CellSection():
    pass


def test_calc_temperature_gradient_PSC2CellSection():
    pass


def test_calc_temperature_gradient_PSC_ISection():
    pass


def test_calc_temperature_gradient_PSC_TSection():
    pass

from sectionproperties.analysis.section import Section
from sectionproperties.pre.geometry import Polygon, Geometry
from moapy.auto_convert import auto_schema
from moapy.data_pre import Point, Points, OuterPolygon
from moapy.data_post import SectionProperty
from moapy.mdreporter import ReportUtil, enUnit
from typing import List, Tuple

@auto_schema(title="Input Polygon", description="Input Polygon")
def input_polygon(points: Points) -> OuterPolygon:
    return OuterPolygon(outerPolygon=points.points)

def convert_points_to_tuple(points: List[Point]) -> Tuple[Tuple[float, float], ...]:
    return tuple((point.x.value, point.y.value) for point in points)

@auto_schema(title="Calculate Section Property", description="Calculate Section Property")
def calc_sectprop(polygon: OuterPolygon) -> SectionProperty:
    geom = Geometry(Polygon(convert_points_to_tuple(polygon.points)))
    geom.create_mesh(mesh_sizes=100.0)

    section = Section(geom)
    section.calculate_geometric_properties()
    section.calculate_warping_properties()
    section.calculate_plastic_properties()
    return SectionProperty(Area=section.get_area(), Asy=section.get_as()[0], Asz=section.get_as()[1], Ixx=section.get_j(), Iyy=section.get_ic()[0], Izz=section.get_ic()[1],
                           Cy=section.get_c()[0], Cz=section.get_c()[1], Syp=section.get_z()[0], Sym=section.get_z()[1], Szp=section.get_z()[2], Szm=section.get_z()[3],
                           Ipyy=section.get_ip()[0], Ipzz=section.get_ip()[1], Zy=section.get_s()[0], Zz=section.get_s()[1], ry=section.get_rc()[0], rz=section.get_rc()[1]
                           )



@auto_schema(title="Report Section Property", description="Report Section Property")
def report_sectprop(sectprop: SectionProperty) -> str:
    rpt = ReportUtil("sectprop.md", "*Section Properties*")
    rpt.add_line_fvu("A_{rea}", sectprop.Area, enUnit.AREA)
    rpt.add_line_fvu("A_{sy}", sectprop.Asy, enUnit.AREA)
    rpt.add_line_fvu("A_{sz}", sectprop.Asz, enUnit.AREA)
    rpt.add_line_fvu("I_{xx}", sectprop.Ixx, enUnit.INERTIA)
    rpt.add_line_fvu("I_{yy}", sectprop.Iyy, enUnit.INERTIA)
    rpt.add_line_fvu("I_{zz}", sectprop.Izz, enUnit.INERTIA)
    rpt.add_line_fvu("C_y", sectprop.Cy, enUnit.LENGTH)
    rpt.add_line_fvu("C_z", sectprop.Cz, enUnit.LENGTH)
    rpt.add_line_fvu("S_{yp}", sectprop.Syp, enUnit.VOLUME)
    rpt.add_line_fvu("S_{ym}", sectprop.Sym, enUnit.VOLUME)
    rpt.add_line_fvu("S_{zp}", sectprop.Szp, enUnit.VOLUME)
    rpt.add_line_fvu("S_{zm}", sectprop.Szm, enUnit.VOLUME)
    rpt.add_line_fvu("I_{pyy}", sectprop.Ipyy, enUnit.INERTIA)
    rpt.add_line_fvu("I_{pzz}", sectprop.Ipzz, enUnit.INERTIA)
    rpt.add_line_fvu("Z_y", sectprop.Zy, enUnit.VOLUME)
    rpt.add_line_fvu("Z_z", sectprop.Zz, enUnit.VOLUME)
    rpt.add_line_fvu("r_y", sectprop.ry, enUnit.LENGTH)
    rpt.add_line_fvu("r_z", sectprop.rz, enUnit.LENGTH)
    return rpt.get_md_text()

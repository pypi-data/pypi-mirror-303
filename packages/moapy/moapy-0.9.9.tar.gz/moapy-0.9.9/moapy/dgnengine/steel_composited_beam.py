import base64
from moapy.auto_convert import auto_schema
from moapy.data_pre import UnitLoads
from moapy.rc_pre import SlabSection, GirderLength
from moapy.steel_pre import SteelMember_EC, ShearConnector
from moapy.dgnengine.base import load_dll, generate_report_xls, read_file_as_binary
from moapy.data_post import ResultBytes

@auto_schema(
    title="EC4 Steel Composite Beam Design",
    description=(
        "This functionality performs the design and verification of steel composite beams "
        "in accordance with Eurocode 4 (EN 1994-1-1). The design process considers key "
        "parameters such as cross-sectional properties, material characteristics, and load "
        "combinations, including the following analyses:\n\n"
        "- Verification of composite action between steel and concrete\n"
        "- Design for bending moments, shear forces, and axial forces\n"
        "- Check for deflections and stability under service conditions\n"
        "- Application of safety factors and load combinations\n\n"
        "The functionality provides detailed design results, including assessments and "
        "recommendations for each design scenario."
    )
)
def report_ec4_composited_beam(steel: SteelMember_EC, shearconn: ShearConnector, slab: SlabSection, leng: GirderLength, load: UnitLoads) -> ResultBytes:
    dll = load_dll()
    json_data_list = [steel.json(), shearconn.json(), slab.json(), leng.json(), load.json()]
    file_path = generate_report_xls(dll, 'Report_EC4_CompositedBeam', json_data_list)
    if file_path is None:
        return ResultBytes(type="md", result="Error: Failed to generate report.")
    return ResultBytes(type="xlsx", result=base64.b64encode(read_file_as_binary(file_path)).decode('utf-8'))


if __name__ == "__main__":
    res = report_ec4_composited_beam(SteelMember_EC(), ShearConnector(), SlabSection(), GirderLength(), UnitLoads())
    print(res)
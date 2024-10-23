import ctypes
import json
import base64
from moapy.auto_convert import auto_schema
from moapy.data_pre import UnitLoads
from moapy.rc_pre import SlabSection, GirderLength
from moapy.steel_pre import SteelMember_EC, ShearConnector
from moapy.dgnengine.base import load_dll, call_func, read_file_as_binary
from moapy.data_post import ResultBytes

@auto_schema(
    title="EC4 Steel Composite Beam Design",
    description="Composite beam that resists bending moment by integrally connecting to reinforced concrete slab and steel beam supporting it by shear connector is designed. Depending on the data that  is entered by users, results of deflection checking, shear connector estimation and Heel drop vibration checking as well as design stress checking applied to each part of composite beam and is automatically calculated."
)
def report_ec4_composited_beam(steel: SteelMember_EC, shearconn: ShearConnector, slab: SlabSection, leng: GirderLength, load: UnitLoads) -> ResultBytes:
    dll = load_dll()
    json_data_list = [steel.json(), shearconn.json(), slab.json(), leng.json(), load.json()]
    file_path = call_func(dll, 'Report_EC4_CompositedBeam', json_data_list)
    if file_path is None:
        return ResultBytes(type="md", result="Error: Failed to generate report.")
    return ResultBytes(type="xlsx", result=base64.b64encode(read_file_as_binary(file_path)).decode('utf-8'))

def calc_ec4_composited_beam(steel: SteelMember_EC, shearconn: ShearConnector, slab: SlabSection, leng: GirderLength, load: UnitLoads) -> dict:
    dll = load_dll()
    json_data_list = [steel.json(), shearconn.json(), slab.json(), leng.json(), load.json(), ctypes.c_void_p(0), ctypes.c_void_p(0)]
    jsondata = call_func(dll, 'Calc_EC4_CompositedBeam', json_data_list)
    dict = json.loads(jsondata)
    print(dict)

if __name__ == "__main__":
    res = calc_ec4_composited_beam(SteelMember_EC(), ShearConnector(), SlabSection(), GirderLength(), UnitLoads())
    print(res)
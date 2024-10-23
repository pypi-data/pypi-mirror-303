import ctypes
import json
import base64
from moapy.auto_convert import auto_schema
from moapy.data_post import ResultBytes
from moapy.steel_pre import SteelConnectMember_EC, SteelPlateMember_EC, ConnectType, SteelBolt_EC, Welding_EC, SteelBoltConnectionForce
from moapy.dgnengine.base import call_func, load_dll, read_file_as_binary

@auto_schema(
    title="Eurocode 3 Steel Bolt Connection Design",
    description=(
        "This functionality performs the design and verification of steel bolt connections "
        "in accordance with Eurocode 3 (EN 1993-1-8). The design process considers key "
        "parameters such as bolt properties, connection geometry, and applied loads, "
        "including the following analyses:\n\n"
        "- Verification of bearing and shear capacities\n"
        "- Design for tensile and shear forces\n"
        "- Check for bolt group effects and slip resistance\n"
        "- Consideration of connection ductility and stability\n\n"
        "The functionality provides detailed design results, including assessments and "
        "recommendations for each connection scenario."
    )
)
def report_ec3_bolt_connection(conn: SteelConnectMember_EC, plate: SteelPlateMember_EC, conType: ConnectType, Bolt: SteelBolt_EC, weld: Welding_EC, force: SteelBoltConnectionForce) -> ResultBytes:
    dll = load_dll()
    json_data_list = [conn.supporting.json(), conn.supported.json(), plate.json(), conType.json(), Bolt.json(), weld.json(), force.json()]
    file_path = call_func(dll, 'Report_EC3_BoltConnection', json_data_list)
    if file_path is None:
        return ResultBytes(type="md", result="Error: Failed to generate report.")
    return ResultBytes(type="xlsx", result=base64.b64encode(read_file_as_binary(file_path)).decode('utf-8'))

def calc_ec3_bolt_connection(conn: SteelConnectMember_EC, plate: SteelPlateMember_EC, conType: ConnectType, Bolt: SteelBolt_EC, weld: Welding_EC, force: SteelBoltConnectionForce) -> dict:
    dll = load_dll()
    json_data_list = [conn.supporting.json(), conn.supported.json(), plate.json(), conType.json(), Bolt.json(), weld.json(), force.json(), ctypes.c_void_p(0), ctypes.c_void_p(0)]
    jsondata = call_func(dll, 'Calc_EC3_BoltConnection', json_data_list)
    dict = json.loads(jsondata)
    print(dict)

if __name__ == "__main__":
    res = calc_ec3_bolt_connection(SteelConnectMember_EC(), SteelPlateMember_EC(), ConnectType(), SteelBolt_EC(), Welding_EC(), SteelBoltConnectionForce())
    print(res)
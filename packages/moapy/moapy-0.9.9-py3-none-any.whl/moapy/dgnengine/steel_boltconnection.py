import base64
from moapy.auto_convert import auto_schema
from moapy.data_post import ResultBytes
from moapy.steel_pre import SteelConnectMember_EC, SteelPlateMember_EC, ConnectType, SteelBolt, Welding_EC
from moapy.dgnengine.base import generate_report_xls, load_dll, read_file_as_binary

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
def report_ec3_bolt_connection(conn: SteelConnectMember_EC, plate: SteelPlateMember_EC, conType: ConnectType, Bolt: SteelBolt, weld: Welding_EC) -> ResultBytes:
    dll = load_dll()
    json_data_list = [conn.supporting.json(), conn.supported.json(), plate.json(), conType.json(), Bolt.json(), weld.json()]
    file_path = generate_report_xls(dll, 'Report_EC3_BoltConnection', json_data_list)
    if file_path is None:
        return ResultBytes(type="md", result="Error: Failed to generate report.")
    return ResultBytes(type="xlsx", result=base64.b64encode(read_file_as_binary(file_path)).decode('utf-8'))


if __name__ == "__main__":
    res = report_ec3_bolt_connection(SteelConnectMember_EC(), SteelPlateMember_EC(), ConnectType(), SteelBolt(), Welding_EC())
    print(res)
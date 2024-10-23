from enum import Enum
import requests

# Enum 값을 리스트로 변환하는 함수
def enum_to_list(enum_class):
    return [member.value for member in enum_class]

class enUnitLength(Enum):
    MM = "mm"
    M = "m"
    IN = "in"
    FT = "ft"

class enUnitForce(Enum):
    N = "N"
    kN = "kN"
    kips = "kips"

class enUnitMoment(Enum):
    kNm = "kN.m"
    kipft = "kip.ft"
    Nmm = "N.mm"
    Nm = "N.m"

class enUnitLoad(Enum):
    kN_m2 = "kN/m2"
    kip_ft2 = "kip/ft2"

class enUnitStress(Enum):
    MPa = "MPa"
    ksi = "ksi"
    
class enUnitThermalExpansion(Enum):
    """Thermal Expansion Coefficient units"""
    PER_CELSIUS = "1/°C"
    # PER_KELVIN = "1/K"

class enUnitAngle(Enum):
    Degree = "degree"
    Radian = "radian"

class enUnitTemperature(Enum):
    Celsius = "celsius"
    Fahrenheit = "fahrenheit"

class enDgnCode(Enum):
    """
    Enum for Design Code
    """
    ACI318M_19 = "ACI318M-19"
    Eurocode2_04 = "Eurocode2-04"

class enEccPu(Enum):
    """
    Enum for Design Code
    """
    ecc = "ecc"
    p_u = "P-U"

class enReportType(Enum):
    """
    Enum for Report Type
    """
    text = "text"
    markdown = "markdown"

# ---- Steel ----
class enBoltMaterialEC(Enum):
    Class46 = "4.6"
    Class48 = "4.8"
    Class56 = "5.6"
    Class58 = "5.8"
    Class68 = "6.8"
    Class88 = "8.8"
    Class109 = "10.9"

class enBoltName(Enum):
    M12 = "M12"
    M16 = "M16"
    M20 = "M20"
    M22 = "M22"
    M24 = "M24"
    M27 = "M27"
    M30 = "M30"
    M36 = "M36"

class enConnectionType(Enum):
    """
    Enum for Connection Type
    """
    Fin_B_B = "Fin Plate - Beam to Beam"
    Fin_B_C = "Fin Plate - Beam to Column"
    End_B_B = "End Plate - Beam to Beam"
    End_B_C = "End Plate - Beam to Column"

class enSteelMaterial_EN10025(Enum):
    S235 = "S235"
    S275 = "S275"
    S355 = "S355"
    S450 = "S450"
    S275NL = "S275N/NL"
    S355NL = "S355N/NL"
    S420NL = "S420N/NL"
    S460NL = "S460N/NL"
    S275ML = "S275M/ML"
    S355ML = "S355M/ML"
    S420ML = "S420M/ML"
    S460ML = "S460M/ML"
    S235W = "S235W"
    S355W = "S355W"
    S460QL1 = "S460Q/QL/QL1"

class enAluminumMaterial_AA(Enum):
    EN_2014_T6 = "2014-T6"
    EN_2014_T6510 = "2014-T6510"
    EN_2014_T6511 = "2014-T6511"
    EN_5083_H111 = "5083-H111"
    EN_5086_H111 = "5086-H111"
    EN_5454_H111 = "5454-H111"
    EN_5454_H112 = "5454-H112"
    EN_5456_H111 = "5456-H111"
    EN_5456_H112 = "5456-H112"
    EN_6061_T6 = "6061-T6"
    EN_6061_T6511 = "6061-T6511"
    EN_6061_T651O = "6061-T651O"
    EN_6063_T5 = "6063-T5"
    EN_6063_T6 = "6063-T6"

# API에서 SectionNameList 데이터를 받아오는 함수
def get_section_names_from_api(codes, types):
    api_url = f"https://moa.rpm.kr-dv-midasit.com/backend/wgsd/dbase/sections/codes/{codes}/types/{types}/names"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("SectionNameList", [])
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

# 동적으로 Enum 클래스를 생성하는 함수
def create_enum_class(class_name, enum_data):
    # Enum 이름에 적합한 형식으로 변환 (공백과 특수문자 등을 처리)
    enum_dict = {name.replace(' ', '_').replace('.', '_'): name for name in enum_data}
    return Enum(class_name, enum_dict)


# 동적으로 생성된 enum 클래스
en_H_EN10365 = create_enum_class('en_H_EN10365', get_section_names_from_api("EN 10365:2017", "H_Section"))
en_H_AISC05_US = create_enum_class('en_H_AISC05_US', get_section_names_from_api("AISC05(US)", "H_Section"))

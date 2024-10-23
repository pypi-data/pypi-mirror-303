import ctypes
import pypandoc
import os
import base64
import json
from moapy.auto_convert import auto_schema
from moapy.data_pre import MemberForce, EffectiveLength, Force, Moment, Length, enUnitForce, enUnitLength, enUnitMoment
from moapy.data_post import ResultBytes
from moapy.steel_pre import SteelMaterial_EC, SteelSection_EN10365, SteelLength_EC, SteelMomentModificationFactor_EC
from moapy.dgnengine.base import call_func, load_dll, read_file_as_binary
import re

def remove_html_blocks(markdown_content):
    # HTML 블록을 제거하기 위한 정규 표현식
    html_block_pattern = re.compile(r'```{=html}\s*<!--\s*-->\s*```', re.DOTALL)
    # 해당 패턴을 빈 문자열로 대체하여 제거
    cleaned_content = re.sub(html_block_pattern, '', markdown_content)
    
    # 또는 주석 부분만 제거하는 경우, 주석 패턴을 찾고 제거
    cleaned_content = re.sub(r'```{=html}\s*', '', cleaned_content)
    cleaned_content = re.sub(r'\s*<!--\s*-->\s*```', '', cleaned_content)

    return cleaned_content

def rtf_to_markdown(file_path):
    # 파일 경로가 bytes로 주어진 경우 문자열로 변환
    if isinstance(file_path, bytes):
        file_path = file_path.decode('utf-8')

    # 파일 경로 검증
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    try:
        # RTF 파일을 Markdown으로 변환
        markdown_content = pypandoc.convert_file(file_path, 'md', format='rtf', extra_args=['--strip-comments'])

        # EMF 이미지 데이터를 찾기 위한 정규 표현식
        emf_pattern = re.compile(r'\\pict\\emfblip(.*?)\\bin', re.DOTALL)
        emf_matches = emf_pattern.findall(markdown_content)

        # EMF 데이터를 base64로 변환
        for match in emf_matches:
            emf_data = match.strip().replace('\n', '').replace('\r', '').replace(' ', '')
            # 16진수 문자열을 바이너리 데이터로 변환
            emf_bytes = bytes.fromhex(emf_data)
            # base64로 인코딩
            base64_emf = base64.b64encode(emf_bytes).decode('utf-8')
            # Markdown 이미지 태그 생성
            markdown_image = f'![EMF Image](data:image/emf;base64,{base64_emf})'
            # 원본 EMF 데이터를 Markdown 이미지 태그로 교체
            markdown_content = markdown_content.replace(match, markdown_image)

        # 불필요한 HTML 블록 제거 (```{=html} <!-- --> ``` 형식)
        markdown_content = remove_html_blocks(markdown_content)

        return markdown_content

    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")
    except Exception as e:
        raise Exception(f"Error converting RTF to Markdown: {e}")

def read_txt_file(file_path):
    if isinstance(file_path, bytes):
        file_path = file_path.decode('utf-8')

    # 파일 경로 검증
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    try:
        # 파일 열기 및 내용 읽기
        with open(file_path, 'r', encoding='utf-16') as file:
            file_content = file.read()
        return file_content
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")

@auto_schema(
    title="Eurocode 3 Beam Design",
    description="Steel column that is subjected to axial force, biaxial bending moment and shear force and steel beam that is subjected to the bending moment are designed. Automatic design or code check for load resistance capacity of cross-sections like H-beam depending on the form of member is conducted."
)
def report_ec3_beam_column(matl: SteelMaterial_EC, sect: SteelSection_EN10365, load: MemberForce, length: SteelLength_EC, eff_len: EffectiveLength, factor: SteelMomentModificationFactor_EC) -> ResultBytes:
    dll = load_dll()
    json_data_list = [matl.json(), sect.json(), load.json(), length.json(), eff_len.json(), factor.json()]
    file_path = call_func(dll, 'Report_EC3_BeamColumn', json_data_list)
    if file_path is None:
        return ResultBytes(type="md", result="Error: Failed to generate report.")
    return ResultBytes(type="xlsx", result=base64.b64encode(read_file_as_binary(file_path)).decode('utf-8'))

def calc_ec3_beam_column(matl: SteelMaterial_EC, sect: SteelSection_EN10365, load: MemberForce, length: SteelLength_EC, eff_len: EffectiveLength, factor: SteelMomentModificationFactor_EC) -> dict:
    dll = load_dll()
    json_data_list = [matl.json(), sect.json(), load.json(), length.json(), eff_len.json(), factor.json(), ctypes.c_void_p(0), ctypes.c_void_p(0)]
    jsondata = call_func(dll, 'Calc_EC3_BeamColumn', json_data_list)
    dict = json.loads(jsondata)
    print(dict)


if __name__ == "__main__":
    res = calc_ec3_beam_column(SteelMaterial_EC(code="ASTM09", name="A36"), SteelSection_EN10365(name="IPE 400"),
                               MemberForce(Fz=Force(value=1000.0, unit=enUnitForce.kN), Mx=Moment(value=500.0, unit=enUnitMoment.kNm), My=Moment(value=200.0, unit=enUnitMoment.kNm),
                                           Vx=Force(value=300.0, unit=enUnitForce.kN), Vy=Force(value=400.0, unit=enUnitForce.kN)),
                               SteelLength_EC(Lb=Length(value=3000.0, unit=enUnitLength.MM)),
                               EffectiveLength(Lx=Length(value=3000.0, unit=enUnitLength.MM), Ly=Length(value=3000.0, unit=enUnitLength.MM)),
                               SteelMomentModificationFactor_EC(c1=1.0, c_mx=1.0, c_my=1.0, c_mlt=1.0))

    print(res)
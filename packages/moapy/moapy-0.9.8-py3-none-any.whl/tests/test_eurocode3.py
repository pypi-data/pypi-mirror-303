import sys
import pytest
import moapy.dgnengine.steel_bc as steel_bc
import moapy.dgnengine.steel_boltconnection as steel_boltconnection
import moapy.dgnengine.steel_composited_beam as steel_composited_beam
from moapy.data_pre import (
    MemberForce, UnitLoads, EffectiveLength, Force, Moment, Length, enUnitForce, enUnitLength, enUnitMoment
)

from moapy.steel_pre import (
    SteelMaterial_EC, SteelSection_EN10365, SteelConnectMember_EC, SteelPlateMember_EC, ConnectType,
    SteelBolt, Welding_EC, SteelMember_EC, ShearConnector, SteelLength_EC, SteelMomentModificationFactor_EC, SteelBoltConnectionForce,
)
from moapy.rc_pre import SlabSection, GirderLength

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_calc_EC3_beamcolumn():
    res = steel_bc.calc_ec3_beam_column(SteelMaterial_EC(code="ASTM09", name="A36"), SteelSection_EN10365(name="IPE 400"),
                                        MemberForce(Fz=Force(value=1000.0, unit=enUnitForce.kN), Mx=Moment(value=500.0, unit=enUnitMoment.kNm), My=Moment(value=200.0, unit=enUnitMoment.kNm),
                                                    Vx=Force(value=300.0, unit=enUnitForce.kN), Vy=Force(value=400.0, unit=enUnitForce.kN)),
                                        SteelLength_EC(Lb=Length(value=3000.0, unit=enUnitLength.MM)),
                                        EffectiveLength(Lx=Length(value=3000.0, unit=enUnitLength.MM), Ly=Length(value=3000.0, unit=enUnitLength.MM)),
                                        SteelMomentModificationFactor_EC(c1=1.0, c_mx=1.0, c_my=1.0, c_mlt=1.0))
    print(res)

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_report_EC3_beamcolumn():
    res = steel_bc.report_ec3_beam_column(SteelMaterial_EC(), SteelSection_EN10365(), MemberForce(), SteelLength_EC(), EffectiveLength(), SteelMomentModificationFactor_EC())

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_calc_boltconnection():
    res = steel_boltconnection.calc_ec3_bolt_connection(SteelConnectMember_EC(), SteelPlateMember_EC(), ConnectType(), SteelBolt(), Welding_EC(), SteelBoltConnectionForce())

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_report_boltconnection():
    res = steel_boltconnection.report_ec3_bolt_connection(SteelConnectMember_EC(), SteelPlateMember_EC(), ConnectType(), SteelBolt(), Welding_EC(), SteelBoltConnectionForce())

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_calc_composited_beam():
    res = steel_composited_beam.calc_ec4_composited_beam(SteelMember_EC(), ShearConnector(), SlabSection(), GirderLength(), UnitLoads())

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_report_composited_beam():
    res = steel_composited_beam.report_ec4_composited_beam(SteelMember_EC(), ShearConnector(), SlabSection(), GirderLength(), UnitLoads())

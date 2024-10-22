import sys
import pytest
import moapy.dgnengine.steel_bc as steel_bc
import moapy.dgnengine.steel_boltconnection as steel_boltconnection
import moapy.dgnengine.steel_composited_beam as steel_composited_beam
from moapy.data_pre import MemberForce, UnitLoads, EffectiveLength
from moapy.steel_pre import SteelMaterial_EC, SteelSection_EN10365, SteelConnectMember_EC, SteelPlateMember_EC, ConnectType, SteelBolt, Welding_EC, SteelMember_EC, ShearConnector, SteelLength_EC, SteelMomentModificationFactor_EC
from moapy.rc_pre import SlabSection, GirderLength

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_report_bc():
    res = steel_bc.report_ec3_beam_column(SteelMaterial_EC(), SteelSection_EN10365(), MemberForce(), SteelLength_EC(), EffectiveLength(), SteelMomentModificationFactor_EC())

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_report_boltconnection():
    res = steel_boltconnection.report_ec3_bolt_connection(SteelConnectMember_EC(), SteelPlateMember_EC(), ConnectType(), SteelBolt(), Welding_EC())

@pytest.mark.skipif(sys.platform.startswith('linux'), reason="Skip test on Linux")
def test_report_composited_beam():
    res = steel_composited_beam.report_ec4_composited_beam(SteelMember_EC(), ShearConnector(), SlabSection(), GirderLength(), UnitLoads())

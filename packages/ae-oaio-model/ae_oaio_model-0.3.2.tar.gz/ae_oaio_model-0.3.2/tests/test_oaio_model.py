""" oaio client unit and integration tests.

"""
import datetime

from ae.oaio_model import NAME_VALUES_KEY, OaiObject, ROOT_VALUES_KEY, STAMP_FORMAT, now_stamp, object_id, stamp_diff


class TestHelpers:
    def test_object_id_main_ids(self):
        assert 'uid' in object_id('uid', 'did', 'aid', 'sid', {})
        assert 'did' in object_id('uid', 'did', 'aid', 'sid', {})
        assert 'aid' in object_id('uid', 'did', 'aid', 'sid', {})
        assert 'sid' in object_id('uid', 'did', 'aid', 'sid', {})

    def test_object_id_values_name(self):
        id = 'name_id'
        values = {NAME_VALUES_KEY: id}
        assert id in object_id('uid', 'did', 'aid', 'sid', values)

    def test_object_id_values_root_path(self):
        id = 'root_path'
        values = {ROOT_VALUES_KEY: id + "/"}
        assert id in object_id('uid', 'did', 'aid', 'sid', values)

    def test_stamp_diff_zero(self):
        stamp = now_stamp()
        assert stamp_diff(stamp, stamp) == 0.0

    def test_stamp_diff(self):
        d1 = datetime.datetime(year=2022, month=3, day=12, hour=9, minute=42, second=24, microsecond=33)
        d2 = datetime.datetime(year=2022, month=3, day=12, hour=9, minute=42, second=36, microsecond=69)
        assert d2 - d1 == datetime.timedelta(seconds=12, microseconds=36)

        s1 = d1.strftime(STAMP_FORMAT)
        s2 = d2.strftime(STAMP_FORMAT)
        assert stamp_diff(s1, s2) == datetime.timedelta(seconds=12, microseconds=36).total_seconds()
        assert stamp_diff(s1, s2) == 12.000036


class TestOaiObject:
    def test_intantiation(self):
        oai_obj = OaiObject(oaio_id='id', cdn_id='cid', client_stamp='stamp')
        assert oai_obj
        assert oai_obj.oaio_id == 'id'
        assert oai_obj.cdn_id == 'cid'
        assert oai_obj.client_stamp == 'stamp'

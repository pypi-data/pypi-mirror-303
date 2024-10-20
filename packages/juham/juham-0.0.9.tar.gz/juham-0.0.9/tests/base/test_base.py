import unittest
from juham.base import Base
from datetime import datetime, timezone


class TestBase(unittest.TestCase):

    def test_constructor(self):
        ok = True
        try:
            object = Base("base")
            self.assertIsNotNone(object)
        except Exception:
            ok = False

        self.assertTrue(ok)

    def test_get_classid(self):
        classid = Base.get_class_id()
        self.assertEqual("Base", classid)

    def test_timestamp(self):
        obj = Base("test")
        # date time string
        ts_str = "2024-07-08T08:48:42Z"
        # the corresponding time stamp in UTC
        ts = 1720428522.340605
        utc_time = datetime.fromtimestamp(ts, timezone.utc)
        utc_timestr = utc_time.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        timestr = obj.epoc2utc(ts)
        self.assertEqual(ts_str, timestr)

    def test_serialization(self):

        # two objects with different attributes
        obj = Base("foo")
        obj.mqtt_host = "titanicus"
        obj.mqtt_port = 99999
        obj.write_attempts = 10
        obj.mqtt_root_topic = "tiptopic"
        with open("foo.json", "w") as f:
            obj.serialize_to_json(f)
        obj2 = Base("bar")

        # assert  all attributes differ before deserialization
        self.assertNotEqual("foo", obj2.name)
        self.assertNotEqual(obj.mqtt_root_topic, obj2.mqtt_root_topic)
        self.assertNotEqual(obj.mqtt_host, obj2.mqtt_host)
        self.assertNotEqual(obj.mqtt_port, obj2.mqtt_port)
        self.assertNotEqual(obj.write_attempts, obj2.write_attempts)

        # deserialize and assert equality
        with open("foo.json", "r") as f:
            obj2.deserialize_from_json(f)
        self.assertEqual("foo", obj2.name)
        self.assertEqual(obj.mqtt_root_topic, obj2.mqtt_root_topic)
        self.assertEqual(obj.mqtt_host, obj2.mqtt_host)
        self.assertEqual(obj.mqtt_port, obj2.mqtt_port)
        self.assertEqual(obj.write_attempts, obj2.write_attempts)


if __name__ == "__main__":
    unittest.main()

import json
from influxdb_client_3 import Point
from juham.base import Base
from juham.base.jmqtt import JMqtt
from juham.web.rcloud import RCloud, RCloudThread


class HomeWizardThread(RCloudThread):
    """Thread that reads HomeWizard's water meter sensor."""

    def __init__(self, topic: str = "", interval: float = 60, url: str = "") -> None:
        """Construct HomeWizard water meter acquisition thread.

        Args:
            topic (str, optional): MQTT topic to post the sensor readings. Defaults to None.
            interval (float, optional): Interval specifying how often the sensor is read. Defaults to 60 seconds.
            url (str, optional): url for reading watermeter. Defaults to None.
        """
        super().__init__()
        self.sensor_topic = topic
        self.interval = interval
        self.device_url = url

    # @override
    def make_url(self) -> str:
        return self.device_url

    # @override
    def update_interval(self) -> float:
        return self.interval

    # @override
    def process_data(self, data):
        super().process_data(data)
        data = data.json()
        msg = json.dumps(data)
        self.publish(self.sensor_topic, msg, qos=1, retain=False)


class HomeWizardWaterMeter(RCloud):
    """Homewizard watermeter sensor."""

    workerThreadId = HomeWizardThread.get_class_id()
    sensor_topic = Base.mqtt_root_topic + "/watermeter"
    url = "http://192.168.86.70/api/v1/data"
    update_interval = 60

    def __init__(
        self,
        name="homewizardwatermeter",
        topic: str = "",
        url: str = "",
        interval: float = 60.0,
    ) -> None:
        """Create Homewizard water meter sensor.

        Args:
            name (str, optional): name identifying the sensor. Defaults to 'homewizardwatermeter'.
            topic (str, optional): Juham topic to publish water consumption readings. Defaults to None.
            url (str, optional): Homewizard url from which to acquire water consumption readings. Defaults to None.
            interval (float, optional): Frequency at which the watermeter is read. Defaults to None.
        """
        super().__init__(name)
        self.active_liter_lpm: float = -1
        self.update_ts: float = 0.0
        if topic != "":
            self.topic = topic
        if url != "":
            self.url = url
        if interval != "":
            self.interval = interval

    # @override
    def on_connect(self, client, userdata, flags, rc):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.sensor_topic)

    # @override
    def on_message(self, client, userdata, msg):
        if msg.topic == self.sensor_topic:
            em = json.loads(msg.payload.decode())
            self.on_sensor(em)
        else:
            super().on_message(client, userdata, msg)

    def on_sensor(self, em: dict) -> None:
        """Handle data coming from the watermeter sensor. Writes the sensor
        telemetry to time series.

        Args:
            em (dict): data from the sensor
        """
        active_liter_lpm = float(em["active_liter_lpm"])
        total_liter_m3 = float(em["total_liter_m3"])
        ts = self.timestamp()
        if (active_liter_lpm != self.active_liter_lpm) or (ts > self.update_ts + 60.0):
            point = (
                Point("watermeter")
                .tag("sensor", "0")
                .field("total_liter", total_liter_m3)
                .field("active_lpm", active_liter_lpm)
                .time(self.epoc2utc(self.timestamp()))
            )
            self.write(point)
            self.info("Water consumption " + str(total_liter_m3))
            self.update_ts = ts
            self.active_liter_lpm = active_liter_lpm

    def run(self):
        self.worker = Base.instantiate(HomeWizardWaterMeter.workerThreadId)
        self.worker.sensor_topic = self.sensor_topic
        self.worker.device_url = self.url
        self.worker.interval = self.update_interval
        super().run()

    def to_dict(self):
        data = super().to_dict()
        data["_homewizardwatermeter"] = {
            "topic": self.sensor_topic,
            "url": self.url,
            "interval": self.update_interval,
        }
        return data

    def from_dict(self, data):
        super().from_dict(data)
        if "_homewizardwatermeter" in data:
            for key, value in data["_homewizardwatermeter"].items():
                setattr(self, key, value)

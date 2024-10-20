import json
from datetime import datetime, timezone

from juham.base import Base, MqttMsg
from juham.shelly.jshelly import JShelly
from juham.web.rcloud import RCloud
from juham.web.rthread import IWorkerThread, RThread


class ShellyPlus1SimulatorThread(IWorkerThread):
    """Thread simulating Shelly Plus 1 wifi relay with four temperature
    sensors."""

    def __init__(self, topic: str = "", interval: float = 60) -> None:
        """Construct thread for simulating data from Shelly1Plus sensors.

        Args:
            topic (str, optional): MQTT topic to post the sensor readings. Defaults to None.
            interval (float, optional): Interval specifying how often the sensor is read. Defaults to 60 seconds.
        """
        super().__init__()
        self.sensor_topic = topic
        self.interval: float = interval
        self.temp: float = 55

    def update_interval(self) -> float:
        return self.interval

    def update(self) -> bool:
        super().update()
        ts = datetime.now(timezone.utc).timestamp()
        self.temp = self.temp + 0.1
        if self.temp > 70:
            self.temp = 50

        data = {
            "method": "NotifyStatus",
            "params": {
                "ts": ts,
                "temperature:100": {
                    "tC": self.temp,  # Temperature in Celsius for sensor1
                },
                "temperature:101": {
                    "tC": self.temp * 0.9,  # Temperature in Celsius for sensor2
                },
                "temperature:102": {
                    "tC": self.temp * 0.8,  # Temperature in Celsius for sensor2
                },
                "temperature:103": {
                    "tC": self.temp * 0.7,  # Temperature in Celsius for sensor2
                },
            },
        }
        msg = json.dumps(data)
        self.publish(self.sensor_topic, msg)
        return True


class ShellyPlus1Simulator(RThread, JShelly):
    """Simulator for ShellyPlus1 wifi relay.

    Spawns an asynchronous thread to generate data from temperature
    sensors.
    """

    workerThreadId = ShellyPlus1SimulatorThread.get_class_id()
    shelly_topic = "/events/rpc"
    update_interval = 60

    def __init__(
        self,
        name="shellyplus1-simulator",
        topic: str = "",
        interval: float = 60.0,
        mqtt_prefix="shellyplus1-a0a3b3c309c4",
    ) -> None:
        """Create Shelly Plus 1 Simulator.

        Args:
            name (str, optional): name of the object. Defaults to 'rhomewizardwatermeter'.
            topic (str, optional): shelly device specific topic. Defaults to None.
            interval (float, optional): _description_. Defaults to None.
            shelly_mqtt_prefix (str, optional): MQTT topic prefix to which to publish shelly events
        """
        super().__init__(name)
        self.mqtt_prefix = mqtt_prefix
        self.active_liter_lpm = -1
        self.update_ts = None
        if topic is not None:
            self.topic = topic
        if interval is not None:
            self.interval = interval
        self.sensor_topic = self.mqtt_prefix + self.shelly_topic

    def on_connect(self, client, userdata, flags, rc):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.mqtt_prefix + self.shelly_topic)

    def on_message(self, client, userdata: MqttMsg, msg):
        if msg.topic == self.sensor_topic:
            em = json.loads(msg.payload.decode())
            self.on_sensor(em)
        else:
            super().on_message(client, userdata, msg)

    def on_sensor(self, em: dict) -> None:
        """Handle data coming from the the Shelly sensors.

        Simply log the event to indicate the presense of simulated device.
        Args:
            em (dict): data from the sensor
        """

    def run(self):
        self.worker = Base.instantiate(ShellyPlus1SimulatorThread.get_class_id())
        self.worker.sensor_topic = self.sensor_topic
        self.worker.interval = self.update_interval
        super().run()

    def to_dict(self):
        data = super().to_dict()
        data["_shellyplus1simulator"] = {
            "shelly_topic": self.shelly_topic,
        }
        return data

    def from_dict(self, data):
        super().from_dict(data)
        if "_shellyplus1simulator" in data:
            for key, value in data["_shellyplus1simulator"].items():
                setattr(self, key, value)

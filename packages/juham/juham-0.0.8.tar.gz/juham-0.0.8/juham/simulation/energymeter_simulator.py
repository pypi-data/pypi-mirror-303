import json
from juham.base import Base
from juham.web import IWorkerThread, RThread


class EnergyMeterSimulatorThread(IWorkerThread):
    """Thread simulating Energy Meter."""

    _power: float = 1000.0  # W
    _power_topic: str = "power"
    _interval: float = 10  # 10 seconds

    def __init__(self) -> None:
        """Construct a thread for publishing power data.

        Args:
            topic (str, optional): MQTT topic to post the sensor readings. Defaults to None.
            interval (float, optional): Interval specifying how often the sensor is read. Defaults to 60 seconds.
        """
        super().__init__()
        self.current_ts: float = self.timestamp()

    @classmethod
    def initialize(cls, power_topic: str, power: float, interval: float):
        """Initialize thread  class attributes.

        Args:
            power_topic (str): topic to publish the energy meter readings
            power (float): power  to be simulated, the default is 1kW
            interval (float): update interval, the default is 10s
        """
        cls._power = power
        cls._interval = interval
        cls._power_topic = power_topic

    # @override
    def update_interval(self) -> float:
        return self._interval

    def publish_active_power(self, ts):
        """Publish the active power, also known as real power. This is that
        part of the  power that can be converted to useful work.

        Args:
            ts (str): time stamp of the event

        """
        dt = ts - self.current_ts
        self.current_ts = ts

        msg = {
            "timestamp": ts,
            "real_a": self._power * dt,
            "real_b": self._power * dt,
            "real_c": self._power * dt,
            "real_total": 3 * self._power * dt,
        }
        self.publish(self._power_topic, json.dumps(msg), 1, True)

    def update(self) -> bool:
        super().update()
        self.publish_active_power(self.timestamp())
        return True


class EnergyMeterSimulator(RThread):
    """Simulator energy meter sensor. Spawns a thread
    to simulate Shelly PM mqtt messages"""

    workerThreadId = EnergyMeterSimulatorThread.get_class_id()
    power_topic = Base.mqtt_root_topic + "/powerconsumption"  # target topic
    update_interval: float = 10
    power: float = 1000.0

    def __init__(
        self,
        name="em",
        interval: float = 0,
    ) -> None:
        """Create energy meter simulator.

        Args:
            name (str, optional): Name of the object. Defaults to 'em'.
            topic (str, optional): MQTT topic to publish the energy meter reports. Defaults to None.
            interval (float, optional): interval between events, in seconds. Defaults to None.
        """
        super().__init__(name)
        self.update_ts: float = 0.0
        if interval > 0.0:
            self.update_interval = interval

    # @override
    def on_message(self, client, userdata, msg):
        if msg.topic == self.power_topic:
            em = json.loads(msg.payload.decode())
            self.on_sensor(em)
        else:
            super().on_message(client, userdata, msg)

    def on_sensor(self, em: dict) -> None:
        """Handle data coming from the energy meter.

        Simply log the event to indicate the presense of simulated device.
        Args:
            em (dict): data from the sensor
        """
        self.debug(f"Simulated power meter sensor {em}")

    def run(self):
        EnergyMeterSimulatorThread.initialize(
            self.power_topic, self.update_interval, self.power
        )
        self.worker = Base.instantiate(EnergyMeterSimulatorThread.get_class_id())
        super().run()

    def to_dict(self):
        data = super().to_dict()
        data["_shellypm"] = {"power_topic": self.power_topic}
        return data

    def from_dict(self, data):
        super().from_dict(data)
        if "_shellypm" in data:
            for key, value in data["_shellypm"].items():
                setattr(self, key, value)

from juham.base import Base


class JShelly(Base):
    """Base class for shelly product family."""

    def __init__(self, name, mqtt_prefix=""):
        """Initialize Shelly apparatus for use.

        Args:
            name (str): name identifying the shelly device.
            mqtt_prefix (str, optional): Device specific MQTT prefix for the topic
            publish their messages to. Defaults to "".
        """
        super().__init__(name)
        self.relay_started = 0
        self.mqtt_prefix = mqtt_prefix
        if self.mqtt_prefix == "":
            self.mqtt_prefix = name

    def elapsed(self, secs: float) -> float:
        """Check if a certain time interval has elapsed and update the start
        timestamp attribute to count elapsed seconds for future calls.

        Args:
            secs (float): The expected elapsed time in seconds since the previous call

        Returns:
            bool: True if the given number of seconds has elapsed, False otherwise.
        """

        tsnow = self.timestamp()
        if tsnow - self.relay_started < secs:
            return False
        self.relay_started = tsnow
        return True

    def to_dict(self):
        data = super().to_dict()
        data["_shelly"] = {"mqtt_prefix": self.mqtt_prefix}
        return data

    def from_dict(self, data):
        super().from_dict(data)
        if "_shelly" in data:
            for key, value in data["_shelly"].items():
                setattr(self, key, value)

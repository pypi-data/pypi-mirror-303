import json
from influxdb_client_3 import Point
from juham.base import Base, MqttMsg


class PowerRecord(Base):
    """Power utilization record.

    This class listens the power utilization message and writes the
    state to time series database.
    """

    def __init__(self, name="powerrecord"):
        """Construct power record object with the given name."""

        super().__init__(name)

    def on_connect(self, client, userdata, flags, rc):
        """Standard mqtt connect notification.

        This method is called when the client connection with the MQTT
        broker is established.
        """
        super().on_connect(client, userdata, flags, rc)
        self.subscribe(Base.mqtt_root_topic + "/power")
        self.debug(f"Subscribed to {Base.mqtt_root_topic}/power")

    def on_message(self, client, userdata, msg: MqttMsg):
        """Standard mqtt message notification method.

        This method is called upon new arrived message.
        """

        m = json.loads(msg.payload.decode())
        if not "Unit" in m:
            return
        unit = m["Unit"]
        ts = m["Timestamp"]
        state = m["State"]
        point = (
            Point("power")
            .tag("unit", unit)
            .field("state", state)
            .time(self.epoc2utc(ts))
        )
        self.write(point)

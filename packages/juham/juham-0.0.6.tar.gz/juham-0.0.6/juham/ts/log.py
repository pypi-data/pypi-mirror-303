import json
from influxdb_client_3 import Point
from juham.base import Base, MqttMsg


class LogRecord(Base):
    """Class recording application events, such as warnigns and errors,
    to time series database."""

    def __init__(self, name="log_record"):
        """Creates mqtt client for recording log events to time series
        database.

        Args:
            name (str): name for the client
        """
        super().__init__(name)

    # @override
    def on_connect(self, client, userdata, flags, rc):
        """Connects the client to mqtt broker.

        Args:
            client (obj): client to be connected
            userdata (any): caller specific data
            flags (int): implementation specific shit

        Returns:
            rc (bool): True if succesful
        """
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(Base.mqtt_root_topic + "/log")

    # @override
    def on_message(self, client, userdata, msg: MqttMsg):
        m = json.loads(msg.payload.decode())
        ts = self.epoc2utc(m["Timestamp"])

        point = (
            Point("log")
            .tag("class", m["Class"])
            .field("source", m["Source"])
            .field("msg", m["Msg"])
            .field("details", m["Details"])
            .field("Timestamp", m["Timestamp"])
            .time(ts)
        )
        try:
            self.write(point)
        except Exception as e:
            self.log_message("Error", f"Cannot write log event {m['Msg']}", str(e))

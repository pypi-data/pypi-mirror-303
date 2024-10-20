import json
from influxdb_client_3 import Point
from juham.base import Base
from juham.shelly.jshelly import JShelly


class Shelly1G3(JShelly):
    """Shelly Plus 1 smart relay time series record.

    Listens MQTT messages from dht22 (am2302) temperature sensors attached to
    Shelly 1 PM Add on module and writes them to time series database.
    """

    shelly_topic = "/events/rpc"  # source topic
    temperature_topic = Base.mqtt_root_topic + "/temperature/"  # target topic
    humidity_topic = Base.mqtt_root_topic + "/humidity/"  # target topic

    def __init__(self, name="shelly1g3-humidity"):
        super().__init__(name)
        self.relay_started = 0

    def on_connect(self, client, userdata, flags, rc):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.mqtt_prefix + self.shelly_topic)

    def on_message(self, client, userdata, msg):
        # optimize out excessive notifications
        tsnow = self.timestamp()
        self.relay_started = tsnow

        m = json.loads(msg.payload.decode())
        mth = m["method"]
        if mth == "NotifyStatus":
            params = m["params"]
            self.on_sensor(params)
        else:
            self.warning("Unknown method " + mth, str(m))

    def on_sensor(self, params: dict) -> None:
        """Map Shelly Plus 1GM specific event to juham format and post it to
        temperature topic.

        Args:
            params (dict): message from Shelly Plus 1 wifi relay
        """
        self.info(f"on_sensor() event {params}")
        ts = params["ts"]
        for key, value in params.items():
            if key.startswith("humidity:"):
                self.on_value(ts, key, value, "humidity", "rh")
            elif key.startswith("temperature:"):
                self.on_value(ts, key, value, "temperature", "tC")

    def on_value(self, ts: float, key: str, value: dict, attr: str, unit: str) -> None:
        sensor_id = key.split(":")[1]
        humidity = value[unit]

        msg = {
            "sensor": sensor_id,
            "timestamp": ts,
            attr: float(humidity),
        }
        self.publish(self.humidity_topic + sensor_id, json.dumps(msg), 1, True)
        self.info(
            f"Humidity reading { self.humidity_topic + sensor_id} {humidity} published"
        )
        try:
            point = (
                Point("ylakerta_humidity")
                .tag("sensor", sensor_id)
                .field(attr, humidity)
                .time(self.epoc2utc(ts))
            )
            self.write(point)
        except Exception as e:
            self.error(f"Writing to influx failed {str(e)}")

    def to_dict(self):
        data = super().to_dict()
        data["_shelly1g3"] = {
            "shelly_topic": self.shelly_topic,
            "temperature_topic": self.temperature_topic,
        }
        return data

    def from_dict(self, data):
        super().from_dict(data)
        if "_shelly1g3" in data:
            for key, value in data["_shelly1g3"].items():
                setattr(self, key, value)

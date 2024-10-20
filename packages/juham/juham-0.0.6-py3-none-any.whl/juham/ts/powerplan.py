import json
from influxdb_client_3 import Point
from juham.base import Base


class PowerPlanRecord(Base):
    """Power plan time series record.

    Listens powerplan topic and updates time series database
    accordingly.
    """

    def __init__(self, name="powerplanrecord"):
        super().__init__(name)

    def on_connect(self, client, userdata, flags, rc):
        super().on_connect(client, userdata, flags, rc)
        self.subscribe(Base.mqtt_root_topic + "/powerplan")

    def on_message(self, client, userdata, msg):
        m = json.loads(msg.payload.decode())
        fom = m["FOM"]
        uoi = m["UOI"]
        ts = m["Timestamp"]

        point = (
            Point("powerplan")
            .tag("unit", m["Unit"])
            .field("state", m["State"])  # 1 on, 0 off
            .field("name", m["Unit"])  # e.g main_boiler
            .field("type", "C")  # C=consumption, S = supply
            .field("power", 16.0)  # kW
            .field("FOM", int(fom))  # figures of merit
            .field("UOI", float(uoi))  # Utilitzation Optimizing Index
            .time(self.epoc2utc(ts))
        )
        self.write(point)

from datetime import datetime
import time
import json

# from typing import override
from influxdb_client_3 import Point

from juham.base import Base
from juham.base.jmqtt import JMqtt
from juham.web import RCloud, RCloudThread


class SpotHintaFiThread(RCloudThread):
    """Thread running SpotHinta.fi.

    Periodically fetches the spot electricity prices and publishes them
    to  'spot' topic.
    """

    _class_id: str = ""
    _spot_topic: str = ""
    _url: str = ""
    _interval: float = 6 * 3600

    def __init__(self):
        super().__init__()
        self._interval = 60

    # @override
    def make_url(self):
        return self._url

    # @override
    def update_interval(self) -> float:
        return self._interval

    # @override
    def process_data(self, data):
        """Publish electricity price message to Juham topic.

        Args:
            data (dict): electricity prices
        """

        super().process_data(data)
        data = data.json()

        spot = []
        for e in data:
            ts = time.mktime(time.strptime(e["DateTime"], "%Y-%m-%dT%H:%M:%S%z"))
            hour = datetime.utcfromtimestamp(ts).strftime("%H")
            h = {
                "Timestamp": ts,
                "hour": hour,
                "Rank": e["Rank"],
                "PriceWithTax": e["PriceWithTax"],
            }
            spot.append(h)
        self.publish(self._spot_topic, json.dumps(spot), 1, True)
        self.info(f"Spot electricity prices published for the next {len(spot)} days")


class RSpotHintaFi(RCloud):

    worker_thread_id = SpotHintaFiThread.get_class_id()
    spot_topic = Base.mqtt_root_topic + "/spot"
    url = "https://api.spot-hinta.fi/TodayAndDayForward"
    update_interval = 6 * 3600

    def __init__(self, name="rspothintafi"):
        super().__init__(name)
        self.active_liter_lpm = -1
        self.update_ts = None

    def on_connect(self, client, userdata, flags, rc):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.spot_topic)

    def on_message(self, client, userdata, msg):
        if msg.topic == self.spot_topic:
            em = json.loads(msg.payload.decode())
            self.on_spot(em)
        else:
            super().on_message(client, userdata, msg)

    def on_spot(self, m):
        """Write hourly spot electricity prices to time series database.

        Args:
            m (dict): holding hourlys spot electricity prices
        """
        for h in m:
            point = (
                Point("spot")
                .tag("hour", h["Timestamp"])
                .field("value", h["PriceWithTax"])
                .time(self.epoc2utc(h["Timestamp"]))
            )
            self.write(point)

    def run(self):
        self.worker = Base.instantiate(RSpotHintaFi.worker_thread_id)
        self.worker._url = self.url
        self.worker._spot_topic = self.spot_topic
        self.worker._interval = self.update_interval
        super().run()

    # @override
    def to_dict(self):
        data = super().to_dict()
        data["_spothintafi"] = {
            "topic": self.spot_topic,
            "url": self.url,
            "interval": self.update_interval,
        }
        return data

    # @override
    def from_dict(self, data):
        super().from_dict(data)
        if "_spothintafi" in data:
            for key, value in data["_spothintafi"].items():
                setattr(self, key, value)

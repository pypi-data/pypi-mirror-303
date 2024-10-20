import json
import math
import time
from influxdb_client_3 import Point
from juham.base import Base
from juham.base.jmqtt import JMqtt
from juham.web.rthread import RThread, IWorkerThread


class RTrackerThread(IWorkerThread):
    """A tracker simulation thread generating and publishing geographic
    coordinates.

    """

    def __init__(self, client=None):
        super().__init__(client)
        self.sensor_topic = None
        self.topic = None
        self.interval = 60
        self.lon = 25.63
        self.lat = 60.95
        self.rad = 3

    def update(self):
        super().update()
        self.update_track(1, "fixed", 0.5, 1.0, 0, 0)
        self.update_track(2, "rotary", 0.7, 1.8, -0.9, 0)

    def update_track(self, id, type, radLon, radLat, offLon, offLat):
        epoc = time.time()
        rec = {
            "ts": epoc,
            "lon": math.sin(epoc / 360000.0) * math.sin(epoc * 0.001) * radLon
            + self.lon
            + offLon,
            "lat": 0.5 * math.cos(epoc / 360000.0) * math.sin(epoc * 0.001) * radLat
            + self.lat
            + offLat,
            "alt": math.cos(epoc / 360000.0) * (10 * id) + 100,
            "fom": math.cos(epoc / 360000.0) * (0.1 * id) * 10 + 100,
            "type": type,
            "id": str(id),
        }
        self.publish(self.topic, json.dumps(rec), qos=1, retain=False)
        self.debug("Track " + str(id) + " moved")


class RTracker(RThread):
    """A tracker automation object. Spawns async thread to generate geographic
    coordinates at specific rate, and writes them to time series database.

    Args:
        RThread (class): super class
    """

    workerThreadId = RTrackerThread.get_class_id()
    lon = 25.636786
    lat = 60.968117
    rad = 3
    update_interval = 60
    topic = Base.mqtt_root_topic + "/tracks"

    def __init__(self, name="rtracker"):
        super().__init__(name)

    def on_connect(self, client, userdata, flags, rc):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        if msg.topic == self.topic:
            em = json.loads(msg.payload.decode())
            self.on_sensor(em)
        else:
            super().on_message(client, userdata, msg)

    def on_sensor(self, msg):
        point = (
            Point("track")
            .tag("id", msg["id"])
            .field("lon", msg["lon"])
            .field("lat", msg["lat"])
            .field("alt", msg["alt"])
            .field("type", msg["type"])
            .field("fom", msg["fom"])
            .time(self.epoc2utc(msg["ts"]))
        )
        self.write(point)
        self.debug(
            f"Track {msg['type']} {msg['lat']} {msg['lon']} recorded to timeseries"
        )

    def run(self):
        self.worker = Base.instantiate(RTracker.workerThreadId)
        self.worker.lon = self.lon
        self.worker.lat = self.lat
        self.worker.rad = self.rad
        self.worker.interval = self.update_interval
        self.worker.topic = self.topic
        super().run()

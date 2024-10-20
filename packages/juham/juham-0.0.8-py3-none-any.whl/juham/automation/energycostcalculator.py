import datetime
from typing import Any
import json
from influxdb_client_3 import Point
from juham.base import Base, MqttMsg
from juham.base.jmqtt import JMqtt


class EnergyCostCalculator(Base):
    """The EnergyCostCalculator class calculates the net energy balance between produced
    and consumed energy for Time-Based Settlement (TBS). It performs the following functions:

    * Subscribes to 'spot' and 'power' MQTT topics.
    * Calculates the net energy and the rate of change of the net energy per hour and per day (24h)
    * Publishes the calculated values to the MQTT net energy balance topic.
    * Stores the data in a time series database.

    This information helps other home automation components optimize energy usage and
    minimize electricity bills.
    """

    topic_in_spot = Base.mqtt_root_topic + "/spot"
    topic_in_powerconsumption = Base.mqtt_root_topic + "/powerconsumption"
    topic_out_net_energy_balance = (
        Base.mqtt_root_topic + "/net_energy_balance"
    )  # hourly energy balance energy for time based settlement
    to_joule_coeff = 1.0 / (1000.0 * 3600)
    energy_balancing_interval: float = 3600

    def __init__(self, name="ecc"):
        super().__init__(name)
        self.current_ts = 0
        self.net_energy_balance_cost_hour = 0
        self.net_energy_balance_cost_day = 0
        self.net_energy_balance_start_hour = self.elapsed_seconds_in_hour(
            self.timestamp()
        )
        self.net_energy_balance_start_day = self.elapsed_seconds_in_day(
            self.timestamp()
        )
        self.spots = []

    # @override
    def on_connect(self, client: object, userdata: Any, flags: int, rc: int):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.topic_in_spot)
            self.subscribe(self.topic_in_powerconsumption)

    # @override
    def on_message(self, client: object, userdata: Any, msg: MqttMsg):
        """Handle MQTT message.

        Args:
            client (object) : client
            userdata (any): user data
            msg (MqttMsg): mqtt message
        """
        ts_now = self.timestamp()

        m = json.loads(msg.payload.decode())
        if msg.topic == self.topic_in_spot:
            self.on_spot(m)
        elif msg.topic == self.topic_in_powerconsumption:
            self.on_powerconsumption(ts_now, m)
        else:
            self.error(f"Unknown event {msg.topic}")

    def on_spot(self, spot: dict):
        """Stores the received per hour electricity prices to spots list.

        Args:
            spot (list): list of hourly spot prices
        """

        for s in spot:
            self.spots.append(
                {"Timestamp": s["Timestamp"], "PriceWithTax": s["PriceWithTax"]}
            )

    def map_prices_to_joules(self, price: float):
        """Convert the given electricity price in kWh to Watt seconds (J)
        Args:
            price (float): electricity price given as kWh
        Returns:
            Electricity price per watt second (J)
        """
        return price * self.to_joule_coeff

    def get_prices(self, ts_prev: float, ts_now: float):
        """Fetch the electricity prices for the given two subsequent time
        stamps.

        Args:
            ts_prev (float): previous time
            ts_now (float): current time
        Returns:
            Electricity prices for the given interval
        """
        prev_price = None
        current_price = None

        for i in range(0, len(self.spots) - 1):
            r0 = self.spots[i]
            r1 = self.spots[i + 1]
            ts0 = r0["Timestamp"]
            ts1 = r1["Timestamp"]
            if ts_prev >= ts0 and ts_prev <= ts1:
                prev_price = r0["PriceWithTax"]
            if ts_now >= ts0 and ts_now <= ts1:
                current_price = r0["PriceWithTax"]
            if prev_price is not None and current_price is not None:
                return prev_price, current_price
        self.error("PANIC: run out of spot prices")
        return 0.0, 0.0

    def calculate_net_energy_cost(self, ts_prev: float, ts_now: float, energy: float):
        """Given time interval as start and stop Calculate the cost over the
        given time period. Positive values indicate revenue, negative cost.

        Args:
            ts_prev (timestamp): beginning time stamp of the interval
            ts_now (timestamp): end of the interval
            energy (float): energy consumed during the time interval
        Returns:
            Cost or revenue
        """
        cost = 0
        prev = ts_prev
        while prev < ts_now:
            elapsed_seconds = ts_now - prev
            if elapsed_seconds > self.energy_balancing_interval:
                elapsed_seconds = self.energy_balancing_interval
            now = prev + elapsed_seconds
            start_per_kwh, stop_per_kwh = self.get_prices(prev, now)
            start_price = self.map_prices_to_joules(start_per_kwh)
            stop_price = self.map_prices_to_joules(stop_per_kwh)
            if abs(stop_price - start_price) < 1e-24:
                cost = cost + energy * elapsed_seconds * start_price
                self.debug(
                    f"Energy cost {str(cost)} e = {str(energy)} J x {str(start_price)} e/J x {str(elapsed_seconds)} s"
                )
            else:
                # interpolate cost over energy balancing interval boundary
                elapsed = now - prev
                if elapsed < 0.00001:
                    self.debug(
                        f"Cost over hour boundary {str(cost)} but elapsed seconds is 0s"
                    )
                    return 0.0
                ts_0 = self.quantize(self.energy_balancing_interval, now)
                t1 = (ts_0 - prev) / elapsed
                t2 = (now - ts_0) / elapsed
                cost = (
                    cost
                    + energy
                    * ((1.0 - t1) * start_price + t2 * stop_price)
                    * elapsed_seconds
                )
                self.debug(
                    f"Cost over hour boundary {str(cost)} e = {str(energy)} J x {str(start_price)} e/J x {str(t1)} s + {str(stop_price)}e x {str(t2)} s"
                )
            prev = prev + elapsed_seconds
        return cost

    def on_powerconsumption(self, ts_now: float, m: dict):
        """Calculate net energy cost and update the hourly consumption attribute
        accordingly.

        Args:
           ts_now (float): time stamp of the energy consumed
           m (dict): Juham MQTT message holding energy reading
        """
        power = m["real_total"]
        if not self.spots:
            self.info("Waiting for electricity prices...")
        elif self.current_ts == 0:
            self.net_energy_balance_cost_hour = 0.0
            self.net_energy_balance_cost_day = 0.0
            self.current_ts = ts_now
            self.net_energy_balance_start_hour = self.quantize(
                self.energy_balancing_interval, ts_now
            )
            self.info(
                f"Energy cost calculator reset at {self.timestampstr(self.net_energy_balance_start_hour) }"
            )
        else:
            # calculate cost
            dp = self.calculate_net_energy_cost(self.current_ts, ts_now, power)
            self.net_energy_balance_cost_hour = self.net_energy_balance_cost_hour + dp
            self.net_energy_balance_cost_day = self.net_energy_balance_cost_day + dp

            # calculate and publish energy balance
            dt = ts_now - self.current_ts  # time elapsed since previous call
            balance = dt * power  # energy consumed/produced in this slot

            self.info(
                f"Net balance cost {self.net_energy_balance_cost_hour * 100.0}, today {self.net_energy_balance_cost_day * 100.0} cents"
            )
            self.publish_net_energy_balance(ts_now, self.name, balance, power)
            self.record_energycost(
                ts_now,
                self.name,
                self.net_energy_balance_cost_hour,
                self.net_energy_balance_cost_day,
            )

            # Check if the current energy balancing interval has ended
            # If so, reset the net_energy_balance attribute for the next interval
            if (
                ts_now - self.net_energy_balance_start_hour
                > self.energy_balancing_interval
            ):
                self.info(
                    f"Energy balance interval {self.net_energy_balance_start_hour} ... {self.timestampstr(ts_now)} completed with cost {self.net_energy_balance_cost_hour} e, resetting"
                )
                self.net_energy_balance_cost_hour = 0.0
                self.net_energy_balance_start_hour = ts_now

            if ts_now - self.net_energy_balance_start_day > 24 * 3600:
                self.info(
                    f"Day {self.net_energy_balance_start_hour} ... {self.timestampstr(ts_now)} completed with cost {self.net_energy_balance_cost_day} e, resetting"
                )
                self.net_energy_balance_cost_day = 0.0
                self.net_energy_balance_start_day = ts_now

            self.current_ts = ts_now

    def record_energycost(
        self, ts_now: float, site: str, cost_hour: float, cost_day: float
    ):
        """Record energy cost/revenue to data storage. Positive values represent
        revenue whereas negative cost.
        Args:
            ts_now (float): timestamp
            site (str): site
            cost_hour (float): cumulative cost or revenue per hour.
            cost_day (float): cost or revenue per day.
        """
        try:
            point = (
                Point("energycost")
                .tag("site", site)
                .field("cost", cost_hour)
                .field("cost_day", cost_day)
                .time(self.epoc2utc(ts_now))
            )
            self.write(point)

        except Exception as e:
            self.error(
                f"Cannot write energycost at {self.timestampstr(ts_now)}", str(e)
            )

    def publish_net_energy_balance(
        self, ts_now: float, site: str, energy: float, power: float
    ):
        """Publish the net energy balance for the current energy balancing interval, as well as
        the real-time power at which energy is currently being produced or consumed (the
        rate of change of net energy).

        Args:
            ts_now (float): timestamp
            site (str): site
            energy (float): cost or revenue.
            power (float) : momentary power (rage of change of energy)
        """
        msg = {"power": power, "energy": energy, "ts": ts_now}
        self.publish(self.topic_out_net_energy_balance, json.dumps(msg), 1, True)

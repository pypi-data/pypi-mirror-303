import math
from datetime import datetime
import pytz
import pvlib
from typing import Any
import json
from juham.base import Base, MqttMsg


class PriceForecast(Base):
    """The PriceForecast class calculates the electricity price forecast for the given
    power levels.

    * Subscribes to 'spot' and 'power' topics.
    * Calculates the electricity price isocurves.
    * Publishes the calculated values to the 'price_forecast' topic.
    * Stores the data in a time series database.

    This information helps other home automation components optimize energy usage and
    minimize electricity bills.
    """

    # topics
    topic_in_spot = Base.mqtt_root_topic + "/spot"
    topic_in_forecast = Base.mqtt_root_topic + "/forecast"
    topic_out_priceforecast = Base.mqtt_root_topic + "/price_forecast"

    # solar power plantOFS
    roof_tilt = 45
    roof_azimuth = 180
    latitude = 61
    longitude = 25.5
    solar_plant_peak_power = 6000 # in Watts!

    def __init__(self, name="price_forecast"):
        super().__init__(name)
        self.current_ts = 0
        self.spots = []
        self.solar = []
        self.priceforecast = []

    # @override
    def on_connect(self, client: object, userdata: Any, flags: int, rc: int):
        super().on_connect(client, userdata, flags, rc)
        if rc == 0:
            self.subscribe(self.topic_in_spot)
            self.subscribe(self.topic_in_forecast)

    # @override
    def on_message(self, client: object, userdata: Any, msg: MqttMsg):
        """Handle MQTT message.

        Args:
            client (object) : client
            userdata (any): user data
            msg (MqttMsg): mqtt message
        """

        m = json.loads(msg.payload.decode())
        if msg.topic == self.topic_in_spot:
            self.on_spot(m)
        elif msg.topic == self.topic_in_forecast:
            self.on_forecast(m)
        else:
            self.error(f"Unknown event {msg.topic}")

    def on_spot(self, price: dict):
        """Stores the received per hour electricity prices to spots list.

        Args:
            spot (list): list of hourly spot prices
        """
        self.spots =  []
        for s in price:
            self.spots.append(
                {"Timestamp": s["Timestamp"], "PriceWithTax": s["PriceWithTax"]}
            )
            print(f"Spot:{s["PriceWithTax"]}")

        if len(self.solar) > 0 and len(self.spots) > 0:
            self.compute_priceforecast(self.spots, self.solar)
            self.info("Price forecast computed")

    def on_forecast(self, forecast: dict):
        """Stores the solar power forecast.This is used for computing price forecast.

        Args:
            spot (list): list of hourly spot prices
        """
        self.solar = []
        for s in forecast:
            if "solarradiation" in s:
                self.solar.append(
                    {"Timestamp" : s["ts"], "solarradiation": s["solarradiation"]}
                )

        if len(self.solar) > 0 and len(self.spots) > 0:
            self.compute_priceforecast(self.spots, self.solar)
            self.info("Price forecast computed")

    def compute_priceforecast(self, spots : list[dict], radiation : list[dict]):
        """This can be positive for periods with positive spot electricity prices and negative for
        periods with negative spot prices. The generated function answers the question: How much would
        it cost to use the available solar power? For example, if the current spot price is €0.10 per kWh,
        the cost reflects the feed-in tariff that is lost when using the electricity for our own
        consumption instead of selling it back to the electricity supplier.

        Args:
            spots (list): spot prices
            radiation (list) : solar radiation forecast, list of powers in kW
        """
        self.priceforecast.clear()

        # solar plant
        price : float = 0
        for spot, power in zip(spots, radiation):
            ts : float = spot["Timestamp"]
            factor : float = self.compute_solar_power_factor(ts, self.roof_tilt, self.roof_azimuth, self.latitude, self.longitude)
            actual_power : float = self.solar_plant_peak_power * factor
            ef = {"Timestamp": spot["Timestamp"], "Source" : "solar", "Price" : 0.0, "Power" : actual_power}
            self.priceforecast.append(ef)
            print(f"Solar: {self.timestampstr(ts)} factor {factor} power{power} : price: {price}")

    def compute_solar_power_factor(self, timestamp: float, roof_tilt: float, roof_azimuth: float, latitude: float, longitude: float) -> float:
        """
        Compute the power factor that, when multiplied with the solar panel's peak power, gives the actual power at the given timestamp.

        Args:
        - timestamp: The current datetime for which the power factor is computed.
        - roof_tilt: Tilt of the roof where panels are mounted (in degrees, 0° = flat, 90° = vertical).
        - roof_azimuth: Direction the roof faces (in degrees, 0° = North, 90° = East, 180° = South, 270° = West).
        - latitude: Latitude of the location.
        - longitude: Longitude of the location.

        Returns:
        - power_factor: A factor (0-1) that represents the percentage of peak power being generated.
        """
        utc_time = datetime.fromtimestamp(timestamp, tz=pytz.utc)
        # Use pvlib to calculate solar position
        solar_position = pvlib.solarposition.get_solarposition(utc_time, latitude, longitude)

        # Get solar zenith (angle between sun and the vertical)
        solar_zenith = solar_position['zenith'].iloc[0]

        # Get solar azimuth (direction of the sun)
        solar_azimuth = solar_position['azimuth'].iloc[0]

        # Convert angles to radians for trig functions
        solar_zenith_rad = math.radians(solar_zenith)
        roof_tilt_rad = math.radians(roof_tilt)
        roof_azimuth_rad = math.radians(roof_azimuth)
        solar_azimuth_rad = math.radians(solar_azimuth)

        # Calculate the cosine of the angle between the sun's rays and the panel's normal
        cos_angle = (math.sin(solar_zenith_rad) * math.sin(roof_tilt_rad) *
                    math.cos(solar_azimuth_rad - roof_azimuth_rad) +
                    math.cos(solar_zenith_rad) * math.cos(roof_tilt_rad))

        # Ensure the factor is not negative (sun might be on the wrong side of the roof)
        power_factor = max(cos_angle, 0)

        return power_factor

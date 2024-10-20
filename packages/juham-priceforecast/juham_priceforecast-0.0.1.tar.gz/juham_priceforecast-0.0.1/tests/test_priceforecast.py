import unittest
from datetime import datetime
import pytz

from juham_priceforecast import PriceForecast


class TestPriceForecast(unittest.TestCase):
    """Unit tests for `PriceForecast` masterpiece."""

    def test_get_classid(self):
        """Assert that the meta-class driven class initialization works."""
        classid = PriceForecast.get_class_id()
        self.assertEqual("PriceForecast", classid)


    def test_compute_solar_power_factor(self):
        forecast : PriceForecast = PriceForecast()
        utc_time : float = datetime(2024, 8, 1, 12, 0, 0, tzinfo=pytz.utc).timestamp()
        factor = forecast.compute_solar_power_factor(utc_time, 45.0, 180, 61, 25)
        self.assertTrue(factor > 0.9)


if __name__ == "__main__":
    unittest.main()

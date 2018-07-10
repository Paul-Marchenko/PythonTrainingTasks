import unittest
import nose
from city_functions import get_city_country


class City_test_case(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country('Kyiv', 'Ukraine')
        self.assertEquals(city_country, 'Kyiv Ukraine')




import unittest
import nose
from city_functions import get_city_country


class City_test_case(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country('Kyiv', 'Ukraine')
        self.assertEquals(city_country, 'Kyiv Ukraine')


class Population_test_case(unittest.TestCase):
    def test_city_country_population(self):
        population = get_city_country('Kyiv', 'Ukraine', '5000')
        self.assertEquals(population, 'Kyiv Ukraine 5000')

import unittest
from city_function import get_country_city_name
class CityTestCases(unittest.TestCase):
    """Testing city_function.py."""
    def test_city_country(self):
        """Do names like 'Nairobi Kenya' work?"""
        details=get_country_city_name('santiago','chile')
        self.assertEqual(details,'Santiago Chile')
    def test_city_country_population(self):
        """The function should take 3 parameters."""
        details=get_country_city_name('santiago','chile','50000000')
        self.assertEqual(details,'Santiago Chile 50000000')
if __name__== '__main__':
    unittest.main()
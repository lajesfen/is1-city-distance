from main import Interface, CoordinateFinder
import unittest

class MainTest(unittest.TestCase):
    def test_success_case(self):
        interface = Interface()
        self.assertEqual(interface.getDistance("Cali", "Colombia", "Lima", "Peru", "CSV"), 1722.31)

    def test_city_does_not_exist(self):
        interface = Interface()
        self.assertEqual(interface.getDistance("Tumbes", "Chile", "Lima", "Peru", "CSV"), None)

    def test_city_is_the_same(self):
        interface = Interface()
        self.assertEqual(interface.getDistance("Lima", "Peru", "Lima", "Peru", "CSV"), 0)

    def test_api_is_down(self):
        finder = CoordinateFinder
        self.assertEqual(finder.getDataFromAPI(self, "Lima", "Peru"), None)

if __name__ == "__main__":
    unittest.main()
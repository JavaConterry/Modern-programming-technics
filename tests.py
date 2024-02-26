import unittest
from dumb_code import Car

class TestClass(unittest.TestCase):
    def test_rotation(self):   
        dumb_car = Car('1234', {'Manufacturer': 'Porsche', 'Model': '911 whats your emergency?'}, 225, 55, 'R', 'V')
        dumb_car.rotate(90)
        self.assertEqual(dumb_car.wheel_angle, 90, 'Your car is dumb in other ways')

if __name__ == '__main__':
    unittest.main()

import unittest
from dumb_code import Car

class TestClass(unittest.TestCase):
    def test_rotation(self):   
        dumb_car = Car('1234', {'Manufacturer': 'Porsche', 'Model': '911 whats your emergency?'}, 225, 55, 'R', 'V')
        dumb_car.rotate(90)
        self.assertEqual(dumb_car.wheel_angle, 90, 'Your car is dumb in other ways')

    def test_details_generating(self):
        dumb_car = Car(None, None, 225, 55, 'R', 'V')
        id_count_of_digits = len(str(dumb_car.model_id))
        self.assertEqual(id_count_of_digits, 4)
        da = 'da' if dumb_car.details is not None else 'ne'
        self.assertEqual(da, 'da')

        
if __name__ == '__main__':
    unittest.main()

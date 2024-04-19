import unittest
from unittest import mock
from io import StringIO
import sys

from modules.Person import Person
from modules.DisabledPerson import DisabledPerson
from modules.Car import Car


class TestClass(unittest.TestCase):
    def test_person_initiate(self):
        pers = Person()
        self.assertEqual(pers.have_a_car(), False, 'Got a car from nowere')


    def test_person_moves_walk(self):
        pers = Person()
        self.assertEqual(pers.walk(), 'I walk', 'Cant walk')

    
    def test_person_moves_drive(self):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            car = Car()
            pers = Person(car)
            pers.drive(['Forward'])
            output = mock_out.getvalue().strip()
        self.assertEqual(output, 'Moving forward')


    def test_person_moves_drive_wrong(self):
        stderr_buffer = StringIO()
        sys.stderr = stderr_buffer

        pers = Person(Car())
        pers.drive(['Up'])
        error = stderr_buffer.getvalue().strip()
    
        sys.stderr = sys.__stderr__
        self.assertEqual(error, 'Unknown car command')


    def test_disabled_person_basic_moves(self):
        dis_pers = DisabledPerson()
        self.assertEqual(dis_pers.can_do, ['Left', 'Right', 'Left Right', 'Right Left', 'Left Left', 'Right Right'])


    def test_adapter_disabled_person_can_impossible(self):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            dis_pers = DisabledPerson(car=Car())
            dis_pers.drive(['Forward'])
            output = mock_out.getvalue().strip()
        self.assertEqual(output, "I can't do that")
        

    def test_adapter_disabled_person_drive(self):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_out:
            dis_pers = DisabledPerson(car=Car())
            dis_pers.drive(['Left Left'])
            output = mock_out.getvalue().strip()
        self.assertEqual(output, 'Moving backward')


if __name__=='__main__':
    unittest.main()
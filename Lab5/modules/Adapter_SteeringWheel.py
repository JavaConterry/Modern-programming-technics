from .Car import Car
from .Person import Person
import sys

class Adapter_to_drive(Person):

    car = Car()

    def __init__(self, car):
        self.car = car

    def walk(self):
        super().walk()
        pass

    def drive(self, arg):
        try:
            match arg:
                case 'Right Right':
                    self.car.move('Forward')
                case 'Left Left':
                    self.car.move('Backward')
                case 'Left':
                    self.car.move('Left')
                case 'Right':
                    self.car.move('Right')
                case 'Right Left' | 'Left Right':
                    self.car.move('Idk')
        except:
            sys.stderr.write('Unrecogrized movement\n')
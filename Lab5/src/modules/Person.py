from abc import abstractmethod
from .Car import Car


class Person:

    def have_a_car(self):
        return self.car != None

    def __init__(self, car : Car = None):
        self.car = car

    @abstractmethod
    def walk(self):
        return 'I walk'

    @abstractmethod
    def drive(self, args=[]):
        if(self.have_a_car==False):
            print('I have nothing to drive')
        else:
            for arg in args:
                self.car.move(arg)
# Person that can do some staff only
from .Person import Person
from .Adapter_SteeringWheel import Adapter_to_drive
from .Car import Car

import sys

class DisabledPerson(Person): #can be an interface to avoid changes

    __can_do_basic = ['Left', 'Right', 'Left Right', 'Right Left', 'Left Left', 'Right Right']

    def __init__(self, car : Car = None, can_do: list =__can_do_basic):
        self.can_do = can_do
        self.car = car

    def walk(self):
        print('I need a wheelchair')

    def drive(self, args=[]):
        if(args==[]):
            return
        if(self.have_a_car):
            wheel_for_disabled = Adapter_to_drive(self.car)
            for arg in args:
                if(arg not in self.can_do):
                    print("I can't do that\n")
                wheel_for_disabled.drive(arg)
        else:
            sys.stderr.write('No car is given')
from modules.DisabledPerson import DisabledPerson
from modules.Car import Car

disabled_pers = DisabledPerson(car=Car())
disabled_pers.walk()
disabled_pers.drive(args=['Right Right', 'Left Left', 'Left', 'Right', 'Right Left'])
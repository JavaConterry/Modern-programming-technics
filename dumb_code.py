# it was said to commit a DUMB code

class Wheel:
    wheel_diameter = 85
    aspect_ratio = 65
    construction_type = 'R'
    load_index = 'H'

    def __init__(self, wheel_diameter, aspect_ratio, construction_type, load_index):
        self.wheel_diameter = wheel_diameter
        self.aspect_ratio = aspect_ratio
        self.construction_type = construction_type
        self.load_index = load_index

    def __str__(self):
        return f"wheel_diameter: {self.wheel_diameter}, aspect_ratio: {self.aspect_ratio}, construction_type: {self.construction_type}, load_index: {self.load_index}"
    
    def rotating(self):
        print('You spin me right `round, baby, right `round')
    


class Car(Wheel):
    model_id = 'XXXXXXXXX'
    details = {'Manufacturer': 'XXXXXX', 'Model': 'xxxxxxx'}

    def __init__(self, model_id, details, wheel_diameter, aspect_ratio, construction_type, load_index):
        self.model_id = model_id
        self.details = details

        Wheel.__init__(self, wheel_diameter, aspect_ratio, construction_type, load_index)

    def __str__(self):
        return f"model_id: {self.model_id}, details: {self.details}, {super().__str__()}"

car = Car('1234', {'Manufacturer': 'Porsche', 'Model': '911 whats your emergency?'}, 225, 55, 'R', 'V')

print(car)
car.rotating()#!!!
# Be happy, now the car is moving! oh sorry, rotating ^_^
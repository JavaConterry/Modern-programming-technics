# it was said to commit a DUMB code

import random

class Wheel:
    wheel_diameter = 85
    aspect_ratio = 65
    construction_type = 'R'
    load_index = 'H'
    wheel_angle = 0

    def __init__(self, wheel_diameter, aspect_ratio, construction_type, load_index):
        self.wheel_diameter = wheel_diameter
        self.aspect_ratio = aspect_ratio
        self.construction_type = construction_type
        self.load_index = load_index
        wheel_angle = 0

    def __str__(self):
        return f"wheel_diameter: {self.wheel_diameter}, aspect_ratio: {self.aspect_ratio}, construction_type: {self.construction_type}, load_index: {self.load_index}"
    
    def rotate(self, value):
        self.wheel_angle += value
    


class Car(Wheel):
    # model_id
    # details

    def generate_model_id(self):
        self.model_id = random.randint(1000, 9999) 

    def generate_dummy_details(self):
        self.details = {'Manufacturer': 'Unknown', 'Model': 'Unknown'}

    def __init__(self, model_id, details, wheel_diameter, aspect_ratio, construction_type, load_index):
        if(model_id is None):
            self.generate_model_id()
        else:
            self.model_id = model_id
        if(details is None):
            self.generate_dummy_details()
        else:
            self.details = details
        

        Wheel.__init__(self, wheel_diameter, aspect_ratio, construction_type, load_index)

    def __str__(self):
        return f"model_id: {self.model_id}, details: {self.details}, {super().__str__()}"





car = Car('1234', {'Manufacturer': 'Porsche', 'Model': '911 whats your emergency?'}, 225, 55, 'R', 'V')

print(car)
# car.rotate(90)#!!!
# Be happy, now the car is moving! oh sorry, rotating ^_^
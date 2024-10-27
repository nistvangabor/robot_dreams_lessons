from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

class Garage:
    def __init__(self):
        self.vehicles = [Car(), Bike()]

    def start_all_engines(self):
        return [vehicle.start_engine() for vehicle in self.vehicles]

garage = Garage()
for engine_sound in garage.start_all_engines():
    print(engine_sound)
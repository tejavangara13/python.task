
# Example: OOP Concepts in Python

from abc import ABC, abstractmethod

class Vehicle(ABC):  
    def __init__(self, brand, model):
        self._brand = brand       
        self.__model = model      
    @abstractmethod
    def vehicle_info(self):  
        pass

    def get_model(self):
        return self.__model  


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)  
        self.fuel_type = fuel_type
    def vehicle_info(self):
        return f"Car: {self._brand}, Model: {self.get_model()}, Fuel: {self.fuel_type}"


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def vehicle_info(self): 
        return f"Bike: {self._brand}, Model: {self.get_model()}, Engine: {self.engine_cc}cc"


car1 = Car("Toyota", "Corolla", "Petrol")
bike1 = Bike("Yamaha", "R15", 155)

print(car1.vehicle_info())   
print(bike1.vehicle_info())

print("Car Model (Private via getter):", car1.get_model())

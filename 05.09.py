# Python OOP Assignment – All topics up to Inheritance

# Base class (Parent Class)
class Vehicle:
    category = "Automobile"
    def __init__(self, brand, model, year):
        # Instance Variables
        self.brand = brand
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def __engine_number(self):
        return "ENG12345"

    def get_engine_details(self):
        return f"Engine Number: {self.__engine_number()}"

    def fuel_type(self):
        return "Petrol or Diesel"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def fuel_type(self):
        return "Petrol"
    
    def car_info(self):
        return f"{self.vehicle_info()} - {self.doors} doors"


class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electric"

    def battery_info(self):
        return f"Battery Capacity: {self.battery_capacity} kWh"


v1 = Vehicle("Tata", "Truck", 2020)
print(v1.vehicle_info())
print(v1.get_engine_details())
print("Category:", Vehicle.category)
print("Fuel:", v1.fuel_type())
print("-" * 40)

c1 = Car("Hyundai", "i20", 2022, 4)
print(c1.car_info())
print("Fuel:", c1.fuel_type())
print("-" * 40)

e1 = ElectricCar("Tesla", "Model S", 2023, 100)
print(e1.vehicle_info())
print(e1.battery_info())
print("Fuel:", e1.fuel_type())

# Base class
class Vehicle:
    def __init__(self, make):
        self.make = make

# Derived class
class Car(Vehicle):
    def description(self):
        return f"This Car is from {self.make}"

# Derived class
class Bike(Vehicle):
    def description(self):
        return f"This Bike is from {self.make}"

car = Car("Toyota")
bike = Bike("Yamaha")

print(car.description()) 
print(bike.description())  


# Output: This Car is from Yamaha
 # Output: This Bike is from Toyota

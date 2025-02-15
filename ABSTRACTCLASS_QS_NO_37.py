from abc import ABC, abstractmethod
# Abstract class
class Car(ABC):
    def __init__(self, make):
        self.make = make
    @abstractmethod
    def description(self):
        pass
    def price(self):
        pass

# Derived class
class Maruti(Car):
    def description(self):
        return f"{self.make} is known for its fuel efficiency."
    def price(self):
        return "The price range is around 5 to 10 lakhs."

# Derived class
class Santro(Car):
    def description(self):
        return f"{self.make} is popular for its compact design."
    def price(self):
        return "The price range is around 4 to 8 lakhs."

# Create instances of Maruti and Santro
maruti = Maruti("Maruti")
santro = Santro("Santro")

print(maruti.description()) 
print(maruti.price())    
print(santro.price())   
print(santro.description())


# Output: The price range is around 5 to 10 lakhs.
# Output: Santro is popular for its compact design.
# Output: The price range is around 4 to 8 lakhs.
# Output: Maruti is known for its fuel efficiency.

"""CP1404/CP5632 Practical - unreliable class (inherits from Car)."""
from car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car"""
    def __init__(self, name, fuel, reliability:float):
        """Initialise an Unreliable instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_distance = 0


    def drive(self, distance):
        """Generate a random number only drive the car if that number is less than the car's reliability"""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, reliablity= {self.reliability}%"
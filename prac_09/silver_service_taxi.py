"""
CP1404/CP5632 Practical
SilverServiceTaxi -> taxi -> Car class
"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that allows SilverServiceTaxi to have a different effective price_per_km."""

    def __init__(self, name, fuel, fanciness:float):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a taxi but with current fare distance."""
        return f"{super().__str__()}"


"""
CP1404/CP5632 Practical
SilverServiceTaxi test
"""
from silver_service_taxi import SilverServiceTaxi

taxi01 = SilverServiceTaxi("Rad car", 100 ,2)
print(taxi01)
taxi01.drive(18)
actual_fare = taxi01.get_fare()
assert actual_fare == 48.8, actual_fare
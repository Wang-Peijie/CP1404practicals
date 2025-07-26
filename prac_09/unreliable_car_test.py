"""CP1404/CP5632 Practical - unreliable car test ."""
from unreliable_car import UnreliableCar

car1 = UnreliableCar("Rad Car", 100, 50)
for i in range(5):
    car1.drive(20)
    print(car1)

car1 = UnreliableCar("Blue Car", 100, 30)
for i in range(5):
    car1.drive(20)
    print(car1)
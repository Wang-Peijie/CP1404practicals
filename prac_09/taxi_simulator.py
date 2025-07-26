"""
CP1404/CP5632 Practical
taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>>"

def main():
    """a function to run a taxi simulator"""
    current_taxi = None
    total_bill = 0.0
    print("Let's drive!")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            pass
        if choice == "D":
            pass
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(MENU).upper()


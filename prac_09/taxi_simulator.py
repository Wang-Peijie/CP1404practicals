"""
CP1404/CP5632 Practical
taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
TAXIS = [Taxi("Prius", 100),SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive\n>>>"

def main():
    """a function to run a taxi simulator"""
    current_taxi = None
    total_bill = 0.0
    print("Let's drive!")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            for i, taxi in enumerate(TAXIS):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(TAXIS):
                    current_taxi = TAXIS[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input. Please enter a number.")
        if choice == "D":
            pass
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(MENU).upper()


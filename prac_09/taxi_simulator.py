"""
CP1404/CP5632 Practical
taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
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
                print(f"{i + 1} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 1 <= taxi_choice <= len(TAXIS):
                    current_taxi = TAXIS[taxi_choice - 1]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    if distance < 0:
                        print("Invalid input, try again")
                    else:
                        current_taxi.drive(distance)
                        trip_cost = current_taxi.get_fare()
                        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                        total_bill += trip_cost
                        current_taxi.start_fare()
                except ValueError:
                    print("Invalid input, try again")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(MENU).upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(TAXIS):
        print(f"{i + 1} - {taxi}")

if __name__ == "__main__":
    main()

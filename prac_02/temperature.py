"""
CP1404/CP5632 - Prac02
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = covert_celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = covert_fahrenheit_celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()


def convert_fahrenheit_celsius():
    """converts from Fahrenheit to Celsius and returns the result"""
    fahrenheit = float(input("fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit():
    """converts from Celsius to Fahrenheit and returns the result"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit



print("Thank you.")

main()
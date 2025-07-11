"""
CP1404/CP5632 Practical 07 - Project management
Estimated time:2 hour
Actual time: 3 hour
"""
from prac_01.menus import user_name
from project import Project
from datetime import datetime
FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects)\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
        ">>>")
def main():
    """"""
    print("Welcome to Pythonic Project Management")
    data = load_file()
    print(f"Loaded {len(data)} projects from {FILENAME}")
    print(data)
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            name = input("Enter the project name:").title()
            print("Project loading")
        elif choice == "S":
            name = input("Enter the project name:").title()
            print("Project saved")
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("invalid input, try again!")
        choice = input(MENU).upper()
    choice = input("Would you like to save to projects.txt?").lower()
    if "yes" in choice:
        pass
        print("Thank you for using custom-built project management software.")
    else:
        print("Thank you for using custom-built project management software.")


def load_file():
    """Load project data from FILENAME and return a list of project."""
    data = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            time = datetime.strptime(parts[1], "%d/%m/%Y").date()
            # eg:31/10/2022
            priority = int(parts[2])
            cost = float(parts[3])
            percentage = int(parts[4])
            data.append(Project(name, time, priority, cost, percentage))
    return data


def get_valid_input(prompt, input_type, blank):
    """Get valid input from the user"""
    valid_input = False
    user_input = None  # Solve the problem of function error
    while not valid_input:
        try:
            user_input = input(prompt)
            if blank and user_input == "":
                return ""
            elif input_type is str:
                valid_input = True
            else:
                user_input = input_type(user_input)
                valid_input = True
        except ValueError:
            print("invalid input, try again!")
    return user_input

main()


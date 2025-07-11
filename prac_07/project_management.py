"""
CP1404/CP5632 Practical 07 - Project management
Estimated time:2 hour
Actual time: 3 hour
"""
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




main()


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
            display_projects(data)
        elif choice == "F":
            user_date = get_valid_input("Show projects that start after date(dd/mm/yyyy):", convert_string_to_date)
            for project in data:
                if project.start_date >= user_date:
                    print(project)
        elif choice == "A":
            print("Let's add a new project")
            name = get_valid_input("Name:",str)
            start_date = get_valid_input("Start date (dd/mm/yy):",convert_string_to_date)
            priority = get_valid_input("Priority:",int)
            cost = get_valid_input("Cost estimate: $", float)
            percent = get_valid_input("Percent complete:",int)
            new_project = Project(name, start_date, priority, cost, percent)
            adjust_priorities(data,new_project)
            data.append(new_project)
        elif choice == "U":
            for i, project in enumerate(data,start=1):
                print(f"{i} {project}")
            user_choice = get_valid_input("Project choice:", int)
            print(data[user_choice - 1])
            new_percent = get_valid_input("New Percentage:", int,blank=True)
            new_priority = get_valid_input("New Priority:", int,blank=True)
            data[user_choice - 1].percentage = new_percent
            data[user_choice - 1].priority = new_priority
        else:
            print("invalid input, try again!")
        choice = input(MENU).upper()
    choice = get_valid_input("Would you like to save to projects.txt?", str).lower()
    if "yes" in choice:
        save_project(data)
        print("Thank you for using custom-built project management software.")
    else:
        print("Thank you for using custom-built project management software.")


def adjust_priorities(data,new_project):
    """Adjust priorities of projects to move for new project"""
    for project in data:
        if project.priority >= new_project.priority:
            project.priority += 1

def display_projects(data):
    """Display projects in priority order"""
    data.sort()
    print("Incomplete projects:")
    for project in data:
        if not project.is_completed():
            print(project)

    print("Completed projects: ")
    for project in data:
        if project.is_completed():
            print(project)



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


def get_valid_input(prompt, input_type, blank=False):
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

def convert_string_to_date(string):
    """Convert a string to a datetime.date"""
    return datetime.strptime(string,"%d/%m/%Y").date()

def save_project(data):
    """Saved projects in FILENAME by formatted string"""
    with open(FILENAME, "w") as out_file:
        out_file.write(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in data:
            out_file.write(project.save_project())

main()
"""CP1404/CP5632 Practical 07 - Project class"""
from datetime import  date
class Project:
    """Represent a project with name, start date, priority, cost, and completion percentage"""

    def __init__(self, name, start_date, priority, cost, percentage):
        """Initialize a Project with name, start date, priority, cost, and completion percentage"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage


    def __repr__(self):
        """Return a string with formatted output"""
        #for test
        # return f"{self.name} {self.start_date} {self.priority} {self.cost} {self.percentage}%"
        formatted_date = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start: {formatted_date}, priorty {self.priority}, estimate: ${self.cost}, completion: {self.percentage}%"


    def __lt__(self, other):
        """Define < based on priority"""
        return self.priority < other.priority


    def is_completed(self):
        """Return True if the project is 100% completed"""
        return self.percentage == 100

    def save_project(self):
        """Return a string for saving to file."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost}\t{self.percentage}\n"
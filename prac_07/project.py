"""CP1404/CP5632 Practical 07 - Project class"""
from datetime import  date
class Project:
    """"""

    def __init__(self, name, start_date, priority, cost, percentage):
        """"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage


    def __repr__(self):
        """"""
        return f"{self.name}, start: {self.start_date}, priorty {self.priorty}, estimate: ${self.cost}, completion: {self.percentage}%"

    def __lt__(self, other):
        """"""
        return self.priority < other.priorty

    def is_completed(self):
        """"""
        return self.percentage == 100
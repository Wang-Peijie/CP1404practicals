"""CP1404/CP5632 Practical 07 - Project class"""
from datetime import  date
class Project:
    """"""

    def __init__(self, name, start_date, priority, cost, percentage):
        """"""
        self.name = name
        self.start_date = start_date
        self.priorty = priority
        self.cost = cost
        self.percentage = percentage


    def __repr__(self):
        """"""
        return f"{self.name} {self.start_date} {self.priorty} {self.cost} {self.percentage}"
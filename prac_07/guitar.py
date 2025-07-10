"""CP1404/CP5632 Practical - guitar class."""
class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name, year, cost):
        """
        Initialise a guitar instance.

        name: string, a name of a guitar
        year: int, The date this guitar was made
        cost: float
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return a string representation of the guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self,current_year):
        """returns how old the guitar is in years"""
        return current_year - self.year

    def is_vintage(self,current_year):
        """returns True if the guitar is 50 or more years old"""
        return self.get_age(current_year) >= 50

    def __lt__(self, other):
        return self.year < other.year
"""CP1404/CP5632 Practical - guitar class."""
class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name='', year=0, cost=0.0):
        """
        Initialise a guitar instance.

        name: string, a name of a guitar
        year: int
        cost: float
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
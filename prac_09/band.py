"""
CP1404/CP5632 Practical
band class
"""
from musician import Musician
from guitar import Guitar

class Band:
    """a Band includes musicians"""
    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a format string to show musicians"""

    def add(self, musician):
        """Add a musician to the band's list of musicians."""
        self.musicians.append(musician)
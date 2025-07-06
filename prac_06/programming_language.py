"""CP1404/CP5632 Practical - language class."""
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

        name: string, a name of this ProgrammingLanguage object
        typing: string, either "Static" or "Dynamic"
        reflection: bool
        year: int
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language has dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

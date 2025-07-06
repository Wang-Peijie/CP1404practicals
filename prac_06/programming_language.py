"""CP1404/CP5632 Practical - language class."""
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a Car instance.

        name: string, a name of this ProgrammingLanguage object
        typing: string
        reflection: bool
        year: int
        """
        self.name = name
        self.typing = typing
        self.reflection = is_dynamic(reflection)
        self.year = year



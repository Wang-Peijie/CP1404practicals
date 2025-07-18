"""
CP1404/CP5632 Practical
dynamic labels
Wang Peijie
Started 19/7/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Alice", "Bob", "Charlie", "Diana"]
class DynamicWidgetsApp(App):
    """Dynamic widgets kivy app to dynamic widget creation."""


    def __init__(self, **kwargs):
        """initialize main app."""
        super().__init__(**kwargs)
        self.names = NAMES

    def build(self):
        """Build the kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels widgets from the NAMES list """


DynamicWidgetsApp().run()
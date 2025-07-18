"""
CP1404/CP5632 Practical
Miles to Kilometres Converter
Wang Peijie
Started 19/7/2025
"""
from kivy.app import App
from kivy.lang import Builder

__author__ = 'Wang Peijie'

MILES_TO_KM = 1.60934


class MilesConvertKmApp(App):
    """This is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

MilesConvertKmApp.run()
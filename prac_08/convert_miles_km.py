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

    def handle_calculation(self):
        """ handle calculation get input number for input_mile and convert to string"""
        value = self.handle_valid_checking()
        result = MILES_TO_KM * value
        self.root.ids.StringProperty.text = str(result)

    def handle_valid_checking(self):
        """handle valid to check input number is correct"""
        try:
            value = float(self.root.ids.input_mile.text)
            return value
        except ValueError:
            return 0

    def handle_plus_minus(self,change):
        """handle plus and minus bottom to let input number +1 or -1"""
        value = self.handle_valid_checking() + change
        self.root.ids.input_mile.text = str(value)
        self.handle_calculation()


MilesConvertKmApp().run()
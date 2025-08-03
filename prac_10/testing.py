"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # Test repeat_string function
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test Car class odometer initialization
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test Car class fuel initialization
    car_default_fuel = Car()
    assert car_default_fuel._fuel == 0, "Car should have default fuel 0"

    car_custom_fuel = Car(fuel=10)
    assert car_custom_fuel._fuel == 10, "Car should set custom fuel correctly"


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('good morning')
    'Good morning.'
    >>> format_sentence('123 test')
    '123 test.'
    """
    if not phrase:
        return ""
    # Capitalize the first character
    formatted = phrase[0].upper() + phrase[1:]
    # Add full stop if not already present
    if not formatted.endswith('.'):
        formatted += '.'
    return formatted


if __name__ == "__main__":
    run_tests()
    doctest.testmod()

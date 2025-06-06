"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When a function receives an argument of the correct type but with an inappropriate value, ValueError will occur.
2. When will a ZeroDivisionError occur?
    When you attempt to divide a number by zero using division or other calculation based on division, ZeroDivisionError will occur.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    if denominator == 0:
        print("Cannot")
    else:
        fraction = numerator / denominator
        print(fraction)
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divided Zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
    This line will print a random integer inclusive of both 5 and 20.
What was the smallest number you could have seen, what was the largest?
    Smallest value: 5
    Largest value: 20


What did you see on line 2?
    This line will print a random number from the range starting at 3 up to 10, in steps of 2.
What was the smallest number you could have seen, what was the largest?
    Smallest value: 3
    Largest value: 9
Could line 2 have produced a 4?
    Yes, it's possible

What did you see on line 3?
    This line will print a random float number between 2.5 and 5.5
What was the smallest number you could have seen, what was the largest?
    Smallest value: 2.5
    Largest value: 5.5
"""
#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(1,100))
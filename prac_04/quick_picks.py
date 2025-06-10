"""
CP1404-prac04
Make a quick pick program for Lottery Ticket
"""
import random
NUMBER_OF_RANDOM = 6
MAX_RANDOM_NUMBER = 45
MIN_RANDOM_NUMBER = 1
number_of_picks = int(input("How many quick picks?"))
total_result = []
for i in range(number_of_picks):
    one_round_result = []
    while len(one_round_result) < NUMBER_OF_RANDOM:
        number = random.randint(MIN_RANDOM_NUMBER,MAX_RANDOM_NUMBER)
        if number in one_round_result:
            pass
        else:
            one_round_result.append(random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER))
    one_round_result.sort()
    total_result.append(one_round_result)
for picks in total_result:
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*picks))
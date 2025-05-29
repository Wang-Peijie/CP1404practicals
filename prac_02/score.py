"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

import random

def main():
    user_score = float(input("Enter score: "))
    user_grade = determine_grade(user_score)
    print(f"Your grade is {user_grade}")
    for i in range(5):
        random_score = random.randint(0, 100)
        print(f"Random score: {random_score}, grade: {determine_grade(random_score)}")
def determine_grade(score):
    """takes a score and returns the corresponding grade"""
    if score > 100 or score < 0:
        return"Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()



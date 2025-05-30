"""
CP1404/CP5632 - Practical02
menu for printing score
"""
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
Enter your choice: """
def main():
    print(MENU)
    choice = input().upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Your score is {score:.2f}")
        elif choice == "P":
            print(f"Your grade is {determine_grade(score)}")
        elif choice == "S":
            print_score_stars(score)
        else:
            print("Invalid input. please try again.")
        print(MENU)
        choice = input().upper()
    print("Farwell!")

def get_valid_score():
    """get a valid score from user"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        score = float(input("Invalid score. Enter score: "))
    return score

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

def print_score_stars(score):
    """Print number of score with stars"""
    score = int(score)
    print("*" * score)

if __name__ == "__main__":
    main()
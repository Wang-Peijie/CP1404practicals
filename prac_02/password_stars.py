"""Password stars prac02"""
MINIMUM_LENGTH = 5
def main():
    user_password = get_password()
    while len(user_password) < MINIMUM_LENGTH:
        print(f"Try again!")
        user_password = get_password()
    print_password_stars(user_password)
def get_password():
    """Get user password input"""
    return input(f"Enter your password (minimum length is {MINIMUM_LENGTH}):")


def print_password_stars(password):
    """Print number of password with stars"""
    print("*" * len(password))


if __name__ == '__main__':
    main()

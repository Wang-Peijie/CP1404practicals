"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Estimate: 20 minutes
Actual:
"""
def main():
    #stores users' emails (unique keys) and names (values) in a dictionary.
    key_to_value = {}
    email = input("Email: ")
    while email != '':
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/n)").upper()
        if choice == "Y" or choice == '':
            key_to_value[name] = email
        else:
            name = input("Name: ")
            key_to_value[name] = email
        email = input("Email: ")



def extract_name(string):
    #Extract a username from user email string
    strings = string.title().split("@")
    print(strings)
    return strings[0]

main()
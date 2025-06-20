"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Estimate: 20 minutes
Actual:  20 min
"""
def main():
    #stores users' emails (unique keys) and names (values) in a dictionary.
    #test text:"wdwad": "wdefad@wqe", "weqe": "ereet.wqewq@qesda.eqeqe", "qweweq": "dsdsf wqes@qwesd,wqedadw@wqeqe"
    name_to_email = {}
    email = input("Email: ")
    while email != '':
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/n)").strip().upper()
        if choice == "Y" or choice == '':
            name_to_email[name] = email
        else:
            name = input("Name: ")
            name_to_email[name] = email
        email = input("Email: ")
    for key,email in name_to_email.items():
        print(f"{key} ({email})")


def extract_name(string):
    #Extract a username from user email string
    name = string.split("@")[0]
    # print(name)
    username = name.replace("."," ").title()
    return username

main()
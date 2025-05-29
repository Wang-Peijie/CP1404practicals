"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = '(H)ello\n(G)oodbye\n(Q)uit\n>>> '
user_name = input("Enter name: ")
print(MENU,end="")
choice = input().upper()
while choice != "Q":
    if choice == "H":
        print("Hello " + user_name)
    elif choice == "G":
        print("Goodbye " + user_name)
    else:
        print("Invalid choice.")
    print(MENU,end="")
    choice = input().upper()
print("Finished.")



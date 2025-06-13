"""
CP1404 - list exercises
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
"""
numbers =[]
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / len(numbers)}")
"""
Ask the user for their username. If the username is in the above list of authorised users, print "Access granted", otherwise print "Access denied"
"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("Enter your username:")
if name not in usernames:
    print("Access denied")
else:
    print("Access granted")
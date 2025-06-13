"""
CP1404 - list exercises
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
"""
numbers =[]
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)
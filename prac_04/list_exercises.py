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
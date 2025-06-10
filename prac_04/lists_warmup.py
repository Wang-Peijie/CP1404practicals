"""Lists warmup"""
#Change the first element of numbers to "ten" (the string, not the number 10)
#Change the last element of numbers to 1
numbers = ["ten", 1, 4, 1, 5, 9, 1]
#Print all the elements from numbers except the first two (slice)
for number in numbers[3:]:
    print(number,end=" ")
#Print whether 9 is an element of numbers
print(9 in numbers)

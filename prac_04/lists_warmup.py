"""Lists warmup"""
#Change the first element of numbers to "ten" (the string, not the number 10)
#Change the last element of numbers to 1
numbers = ["ten", 1, 4, 1, 5, 9, 1]
#Print all the elements from numbers except the first two (slice)
print(*numbers[2:])
#or
for number in numbers[2:]:
    print(number,end=" ")
print()
#or
print(" ".join([str(n) for n in numbers[2:]]))
#or
[print(n,end=" ")for n in numbers[2:]]
print()
#Print whether 9 is an element of numbers
print(9 in numbers)

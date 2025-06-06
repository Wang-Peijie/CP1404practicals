#Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
FILENAME01 = "name.txt"
user_name = input("Enter some name:")
with open(FILENAME01,'w') as out_file:
    print(user_name,file=out_file)

#In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output)
in_file = open(FILENAME01,'r')
name = in_file.readline()
print(f"Hi {name}")
in_file.close()

#Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
FILENAME02 = "numbers.txt"
with open(FILENAME02,'r') as in_file:
    number01 = int(in_file.readline())
    number02 = int(in_file.readline())
result = number01 + number02
print(result)

#Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers. Use with instead of open and close for this question.
with open(FILENAME02,"r") as in_file:
    lines = in_file.readlines()
    total_number = sum(int(line) for line in lines)
print(total_number)

"""
a program to count the occurrences of words in a string. The program should ask the user for a string, then print
the counts of how many of each word are in the string.
Estimate: 20 minutes
Actual:    minutes
"""
word_to_length = {}
text = input("Enter a sentence:")
text_list = text.split()
for word in text_list:
    word_to_length[word] = len(word)
max_word_length = max((len(word)) for word in text_list)
print(max_word_length)
# print(word_to_lenght)
print(f"text = {text}")
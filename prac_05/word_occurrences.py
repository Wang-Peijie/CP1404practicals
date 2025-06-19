"""
a program to count the occurrences of words in a string. The program should ask the user for a string, then print
the counts of how many of each word are in the string.
Estimate: 20 minutes
Actual:   20 minutes
"""
word_to_count = {}
text = input("Enter a sentence:")
texts = text.split()
for word in texts:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
max_word_length = max((len(word)) for word in texts)
# print(max_word_length)
# print(word_to_count)
print(f"text = {text}")
for word in word_to_count:
    print(f"{word:{max_word_length}} = {word_to_count[word]}")

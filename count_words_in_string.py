"""
Write a python function to count words in a string (TSRS)
"""

# defining a function "count_words()" which takes a string as an argument
# and returns number of words
def count_words(string):
    return len(string.split(' '))

# taking input from the user
string = input("Enter a string : ")

# printing number of words in string
print("Total number of words :", count_words(string))
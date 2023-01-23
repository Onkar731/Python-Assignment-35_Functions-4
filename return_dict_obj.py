"""
Write a python function to filter out words from a text starting from same alphabet
and store them in a list. Now create a dict with alphabets as key-values and list
of words starting from that alphabet as data values. Take text as an argument and
return dict object (TSRS)
"""

# defining a function "filter_words()" which takes string as an agrument and
# returns a dictionary object which has key-values and data-values
def filter_words(string):
    temp_list = string.split(' ')
    
    # definig a word_dict() 
    word_dict = dict()
    
    for e in temp_list:
        word_dict[e[0]] = [w_name for w_name in temp_list if e[0] == w_name[0]]
    
    return word_dict


# taking input from the user
string = input("Enter a string : ")

# printing a word dictionary
print("Words dictionary :")
word_dict = filter_words(string)
for k,v in word_dict.items():
    print(k, v)
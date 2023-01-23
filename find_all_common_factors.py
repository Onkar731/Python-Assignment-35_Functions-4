"""
Write a python function to find all the common factors of two given numbers.
Return a tuple of such factors (TSRS)
"""

# defining a function "find_common_factors()" which takes two numbers as an 
# argument and returns a tuple of common factors of these two numbers
def find_common_factors(num1, num2):
    # finding a smallest ones
    smallest = num1 if num1<num2 else num2

    # defining a temp_list
    temp_list = [1]
    i = 2
    while i <= smallest:
        if num1%i == 0 and num2%i == 0:
            temp_list.append(i)
        i += 1
    
    # returning a tuple of common factors
    return tuple(temp_list)

# taking input from the user
num1, num2 = int(input("Enter two numbers : ")), int(input())

# printing all common factors
print("All common factors :", find_common_factors(num1, num2))
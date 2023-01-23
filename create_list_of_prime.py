"""
Write a python function to create a list of prime numbers between two given
numbers (TSRS)
"""

# defining a function to check whether the number is prime or not
# which takes a number as an argument and returns True or False
def is_prime(num):
    i = 2
    while i<num:
        if num%i == 0:
            return False
        i += 1
    if i == num:
        return True
    

# defining a function "list_prime()" which takes two numbers as an arguments
# and returns list of prime numbers
def list_prime(start,end):
    prime_list = list()
    while start <= end:
        if is_prime(start):
            prime_list.append(start)
        start += 1
    
    return prime_list

# taking input from the user
start, end = int(input("Enter start and end number to get prime number : ")), int(input())

# printing list of prime numbers between two numbers
print("List of prime numbers :", list_prime(start, end))
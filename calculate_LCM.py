"""
Write a python function to calculate LCM of two number (TSRS)
"""

# defining a function "lcm()" which takes two numbers as an argument
# and returns lcm of two numbers
def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
        
    while True:
        if greater%num1 == 0 and greater%num2 == 0:
            return greater
        greater += 1


# taking input from the user
num1, num2 = int(input("Enter two numbers : ")), int(input())

# printing lcm of two numbers
print("LCM :", lcm(num1, num2))
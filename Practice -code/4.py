#Operators in Python

'''
Write a Python program that takes two numbers as input from the user and checks if:

Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a & b > 10)
print(a | b < 5)
print(a != b)

#Logical operators
x = 5
y = 10
z = 15

# and operator
print(x > 0 and y > 5)  # Output: True (both conditions are True)

# or operator
print(x > 10 or z > 10)  # Output: True (one of the conditions is True)

# not operator
print(not(x > 10))  # Output: True (reverses False to True)

'''
Create a Python program that asks the user for their age and prints:

"You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.
'''

age=int(input("Enter your age: "))
if (age >= 18):
    print("You are an adult")
else:
    print("You are a minor")

'''
Membership Operator Exercise: Write a Python program that:

Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in).
'''
Name=input("Enter your name: ")
print("a" in Name)
print("Python" not in Name)

'''
Bitwise Operator Task: Given two integers, write a Python program that:

Prints the result of a & b, a | b, and a ^ b.
Shifts the bits of a two positions to the left (a << 2).
Shifts the bits of b one position to the right (b >> 1).
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a & b)
print(a | b)
print(a ^ b)
print(a << 2)
print(b >> 1)
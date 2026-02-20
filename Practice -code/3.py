#Input/Output, String manipulation, and Comments
#Simple greeting program
Name=input("Enter your name: ")
Age=int(input("Enter your age: "))
College=input("Enter your college name: ")
Branch=input("Enter your branch: ")
print("Hello, "+ Name + " ! you are " + str(Age) + " yeas old, studing " + Branch + " at " + College + ".")
#print(f" Hello, {Name}! you are {Age} years old, studying {Branch}, at {College}.")

#String Manipulation
comment=("Python is awsome  ")
print(comment)
print(comment.upper())
print(comment.lower())
print(comment.replace("Python is awsome","_Python is awsome_!"))
print(comment.strip())

#Charachter count:Write a Python program that:Asks the user for a string.Prints how many characters are in the string, excluding spaces.
Name=input("Enter your name: ")
count=len(Name)
print("Number of characters: ",count)

#Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:
print("Hello\n\tWorld\n This is a Backslash \\")
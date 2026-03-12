#Decision making(Conditional statements if,else,elif)
#if statement
marks=50
if marks == 50:
    print("Excellent") # if condition satisfies then it prints the statement

#else statement
marks=50
if marks == 50:
    print("Excellent")
else:
    print("Bad") # if condition fails the alternative condition be executed

#elif statement
if marks == 50:
    print("Excellent")
elif marks == 30:
    print("Good")
else:
    print("Bad")

#Comparision operators in if statement(==, !=, <, >, <=, >=)
avg_attendence = 75
if avg_attendence >= 75:
    print("Your are elligible for exam")
else:
    print("Your are not elligible for exam")

#Logical operators in if statement(and, or, not)
avg_attendence = 75
have_permission = True
if avg_attendence >= 75 and have_permission:
    print("Elligible for exam")
else:
    print("Not elligible for exam")

#Nested if statements 
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is Zero")
    elif num < 10:
        print("Small Positive Number")
    else:
        print("Large Positive Number")
else:
    print("Negative Number")

    
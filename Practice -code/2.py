# Variables in Python

x=4 #Assigning integer value to a variable
y="Nithya" #Assigning string value to a variable

age=20
name="Nithya"
is_student=True

#Data types in Python
x=10
print(type(x))
print(type(name))
print(type(is_student))

#Type conversion 
y=float(age)
print(y)

#Arithmetic Operators

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

#Swapping using a third variable
a=3
b=8
print("Before swapping:")
print("a=", a)
print("b=", b)

temp=a
a=b
b=temp

print("after swapping:")
print("a=", a)
print("b=", b)

#Swapping without third variable
a=4
b=6

print("Before swapping:")
print("a=", a)
print("b=", b)

a=a+b #We can also do easily as a,b=b,a
b=a-b
a=a-b

print("after swapping:")
print("a=", a)
print("b=", b)



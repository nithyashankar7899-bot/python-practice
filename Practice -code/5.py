#Lits in python
#Creating list
Items=["Coffee powder", "Milk", "Sugar","Busicuits"]
Quantity=[2,1,1,3]
print(Items)
#Accessing List Elements
Items=["Coffee powder", "Milk", "Sugar","Busicuits"]
print(Items[2])
print(Items[-1])

#Adding elements
Items[1]= "Tea powder"
print(Items)
Items.append("Milk")
Items.insert(-1, "Jaggery")
print(Items)
#Removing elements
Items.remove("Milk")
print(Items)
Items.pop()
print(Items)
Items.clear()
print(Items)

#Slicing list
Items=["Coffee powder", "Milk", "Sugar","Busicuits"]
print(Items[1:3])
print(len(Items))
print(sorted(Items))
print(Items.index("Milk"))

#Nested List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)

'''
List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.
'''
Lang=["Kannada", "English", "Hindi", "Tamil"]
print(Lang)
Lang.append("Telugu")
Lang.insert(2,"Marati")
print(Lang)
Lang.pop(2)
print(Lang)

'''
Reverse and Sort a List: Create a list of numbers and:

Sort it in descending order.
Reverse the sorted list and print it.
'''
numbers=[2,5,7,0,8,1]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
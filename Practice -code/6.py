#Tuples 
fruits = ("apple", "mango", "strawberry")
even_numbers = (2, 4, 6, 8)
events = ("Holi",) # when there exits a single element
print(fruits)
print(even_numbers,events)

#Accesing tuples
print(fruits[2])
print(even_numbers[1:3])
print(events[::])

#Tuple operations
combined_tuple= fruits+ even_numbers
print(combined_tuple)
print((fruits)*2) #Repetition
print(6 in even_numbers) #Checking Membership
print("mango" in fruits)

#Tuple methods
fruits = ("apple", "mango", "strawberry", "apple")
print(fruits.count("apple")) #count()
print(even_numbers.count(4))
print(fruits.index("apple")) #index() of first appearence
print(even_numbers.index(8))

#Sets
fruits= {"apple", "mango", "strawberry"}
even_numbers = {2, 4, 6, 8}
items = set() #empty set , {} --> creates an empty dictionary.

#set operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
print(union_set)

union_sets = fruits & even_numbers
union_set = set1 & set2 #returns common in both sets
print(union_sets)
print(union_set)
union_set = set1 - set2 #returns elements that are in firts set but not in second set
print(union_set)
union_set = set1 ^ set2
print(union_set) #returns elements that are in either of the sets but not in both.

#Set methods
fruits.add("pineapple")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.discard("orange")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)

"""
Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?
"""
fruits = ["apple", "mango", "strawberry"]
fav_fruits = tuple(fruits)
print(fav_fruits)
lvd_fruits = set(fruits)
print(lvd_fruits)
#fav_fruits.add("orange")
#print(fav_fruits) #error(tuples cannot be altered)
lvd_fruits.add("orange")
print(lvd_fruits)
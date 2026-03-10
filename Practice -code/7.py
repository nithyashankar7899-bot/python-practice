#Dictionaries 
fruits_color = {"apple":"red", "pineapple":"yellow", "strawberry":"pink"}
print(fruits_color)

#Accessing Dictionary Elements
print(fruits_color["apple"]) #OR
print(fruits_color.get("strawberry"))
print(fruits_color.get("orange")) 

#Adding and Updating Dictionary elements
fruits_color["strawberry"] = "dark red" #uptading
print(fruits_color)
fruits_color["grapes"]="green"
print(fruits_color)

#Removing elements from Dictionary
poping = fruits_color.pop("pineapple")
print(fruits_color)
del fruits_color["grapes"]
print(fruits_color)
fruits_color.clear()
print(fruits_color)

#Dictionary methods
fruits_color = {"apple":"red", "pineapple":"yellow", "strawberry":"pink"}
print(fruits_color.keys())
print(fruits_color.values())
print(fruits_color.items())
new_fruits = {"mango":"yellow"}
fruits_color.update(new_fruits)
print(fruits_color)

'''
Nested Dictionary Practice (Simple for now):

Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
Access and print the favorite food of one friend.
'''
friends = {
    "Frnd1":{
        "name":"Nithya", 
             "fav_sub":"Math",
             "fav_food":"Dosa"},

             "Frnd2":{"name":"Gagan",
                      "fav_sub":"Science", 
                      "fav_food":"Biryani"}
}
print(friends["Frnd2"]["fav_food"])
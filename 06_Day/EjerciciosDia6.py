#Excercises: Level 1
#Create an empty tuple
empty_tuple = ()

#Create a tuple containing names of your 
# sisters and your brothers 

Familiy = ('Diego', 'Mauricio', 'Emilio', 'Fernanda')

#Join brothers and sisters tuples and assign it to siblings
siblings = Familiy

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of 
# your father and mother and assign it to family_members
family_members = ('Diego', 'Mauricio', 'Emilio', 'Fernanda', 'Omar', 'Lorena', 'Yveth')

#Exercises: Level 2
#Unpack siblings and parents from family_members
print("Siblings"[0:3])
print("Parents"[5:7])

#Create fruits, vegetables and animal products tuples. 
# Join the three tuples 
# and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'cherry','grape','strawberry')
vegetables = ('lettuce', 'cucumber', 'carrot', 'tomato', 'onion')
animal_products = ('meat', 'milk', 'egg', 'butter', 'cheese')

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = fruits + vegetables + animal_products

#Slice out the middle item or 
# items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[7:8])

#Slice out the first three items and the 
# last three items from food_staff_lt list
first_three_items = food_stuff_tp[:3]
last_three_items = food_stuff_tp[-3:]
print("first_three_items", "last_three_items")

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


print("Revisado")
# ------ Tuples ------
#A tuple is a collection of different data types which is ordered and unchangeable (immutable).
# Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values.
# We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).
# Unlike list, tuple has few methods. Methods related to tuples:
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

# ------ Creating Tuples ------

empty_tuple = tuple()
print('empty_tuple: ', empty_tuple)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('fruits: ', fruits)
print('Length of fruits: ', len(fruits))

# ------ Accessing Tuple Items ------

# Positive Indexing
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) -1
last_fruit = fruits[last_index]
print('First Fruit: ', first_fruit)
print('Second Fruit: ', second_fruit)
print('Last Fruit: ', last_fruit)

# Negative Indexing
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print('First Fruit: ', first_fruit)
print('Second Fruit: ', second_fruit)
print('Last Fruit: ', last_fruit)

# ------ Slicing Tuples ------

# We can slice out a sub-tuple by specifying a range of indexes where to start and
# where to end in the tuple, the return value will be a new tuple with the specified items.

# Positive Indexing
all_fruits = fruits[0:4]    # all items
print('all_fruits: ', all_fruits)

all_fruits= fruits[0:]      # all items
print('all_fruits: ', all_fruits)

orange_mango = fruits[1:3]  # doesn't include item at index 3
print('orange_mango: ', orange_mango)

orange_to_the_rest = fruits[1:]
print('orange_to_the_rest: ', orange_to_the_rest)

# Negative Indexing
all_fruits = fruits[-4:]    # all items
print('all_fruits: ', all_fruits)

orange_mango = fruits[-3:-1]  # doesn't include item at index 3
print('orange_mango: ', orange_mango)

orange_to_the_rest = fruits[-3:]
print('orange_to_the_rest: ', orange_to_the_rest)

# ------ Changing Tuples To Lists ------

# We can change tuples to lists and lists to tuples.
# Tuple is immutable, if we want to modify a tuple we should change it to a list.
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# ------ Checking An Item In A Tuple ------

# We can check if an item exists or not in a tuple using in, it returns a boolean.
print('Orange in fruits?: ', 'orange' in fruits) # True
print('Pear in fruits?: ', 'pear' in fruits)  # False
#fruits[0] = 'apple'      # TypeError: 'tuple' object does not support item assignment

# ------ Joining Tuples ------

# We can join two or more tuples using + operator
fruits = ('banana', 'orange', 'mango', 'lemon')
print('fruits: ', fruits)
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
print('vegetables: ', vegetables)
fruits_and_vegetables = fruits + vegetables
print('fruits_and_vegetables: ', fruits_and_vegetables)

# ------ Deleting Tuples ------

# It is not possible to remove a single item in a tuple
# but it is possible to delete the tuple itself using del.
del fruits

# ------ Exercises 1 ------

# 1: Create an empty tuple
print('1: ')
games = tuple()
print('games: ', games)

# 2: Create a tuple containing names
print('2: ')
names = ('John', 'Mary', 'Rob', 'Saoirse')
print('names: ', names)

# 3: Join brothers and sisters tuples and assign it to siblings
print('3: ')
brothers = ('John', 'Rob')
print('brothers: ', brothers)
sisters = ('Mary', 'Saoirse')
print('sisters: ', sisters)
siblings = brothers + sisters
print('siblings: ', siblings)

# 4: How many siblings do you have?
print('4: ')
no_of_siblings = len(siblings)
print('No. of Siblings: ', no_of_siblings)

# 5: Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print('5: ')
print('siblings tuple: ', siblings)
siblings = list(siblings)
print('siblings list: ', siblings)
siblings.append('Kitty')
siblings.append('Red')
print('siblings list: ', siblings)
family_members = tuple(siblings)
print('family_members: ', family_members)
print('siblings: ', siblings)

# ------ Exercises 2 ------

# 1: Unpack siblings and parents from family_members
print('1: ')
family_members = list(family_members)
print('family_members list: ', family_members)
*siblings, mom, dad = family_members
print('siblings: ', siblings)
print('mom: ', mom, ' dad: ', dad)
parents = [mom, dad]
print('parents: ', parents)
siblings = tuple(siblings)
parents = tuple(parents)
print('siblings tuple: ', siblings)
print('parents tuple: ', parents)

# 2: Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
print('2: ')
fruits = ('Apple', 'Orange', 'Pear')
veg = ('Carrot', 'Onion', 'Garlic')
meat = ('Beef', 'Chicken', 'Pork')
print('fruits: ', fruits)
print('veg: ', veg)
print('meat: ', meat)
food_stuff_tp = meat + veg + fruits
print('food_stuff_tp: ', food_stuff_tp)

# 3: Change the food_stuff_tp tuple to a food_stuff_lt list
print('3: ')
food_stuff_lt = list(food_stuff_tp)
print('food_stuff_lt: ', food_stuff_lt)

# 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print('4: ')
length = len(food_stuff_lt)
print('Length of food_stuff_lt: ', length)
middle_item = food_stuff_lt[length // 2]
print('middle_item: ', middle_item)
food_stuff_lt.remove(middle_item)
print('food_stuff_lt: ', food_stuff_lt)

# 5: Slice out the first three items and the last three items from food_stuff_lt list
print('5: ')
first_three = food_stuff_lt[:3]
print('first_three: ', first_three)
last_three = food_stuff_lt[-3:]
print('last_three: ', last_three)

# 6: Delete the food_staff_tp tuple completely
print('6: ')
del food_stuff_tp

# 7: Check if an item exists in tuple: Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
print('7: ')
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('nordic_countries: ', nordic_countries)
print('Estonia?: ', 'Estonia' in nordic_countries)
print('Iceland?: ', 'Iceland' in nordic_countries)

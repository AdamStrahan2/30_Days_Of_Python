# ------ Sets ------
# Set is a collection of unordered and un-indexed distinct elements.
# In Python set is used to store unique items, and it is possible to find the union, intersection,
# difference, symmetric difference, subset, super set and disjoint set among sets.

# ------ Creating Sets ------

empty_set = set()
print(empty_set)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
print('Length of fruits: ', len(fruits))

# ------ Accessing Items In Sets ------

# We use loops to access items. We will see this in loop section

# ------ Checking an Item In Sets ------

print('Mango in fruits?: ', 'mango' in fruits ) # True
print('Pear in fruits?: ', 'pear' in fruits ) # False

# ------ Adding Items to Sets ------

# Add one item using add()
fruits.add('lime')
print('fruits: ', fruits)

# Add multiple items using update() The update() allows to add multiple items to a set.
# The update() takes a list argument.
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print('fruits: ', fruits)

# ------ Removing Items From Sets -------

# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors,
# so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
fruits.remove('potato')
print('fruits: ', fruits)
#fruits.remove('beef')       returns KeyError
fruits.discard('cabbage')
print('fruits: ', fruits)
fruits.discard('beef')      # No error
print('fruits: ', fruits)

# The pop() methods remove a random item from a list and it returns the removed item.
fruits.pop()  # removes a random item from the set
print('fruits: ', fruits)
removed_item = fruits.pop()
print('Removed Item: ', removed_item)

# ------ Clearing Items From Sets ------

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('fruits: ', fruits)
fruits.clear()
print('fruits: ', fruits) # set()

# ------ Deleting Sets ------

del fruits

# ------ Converting Lists To Sets ------

# We can convert list to set and set to list.
# Converting list to set removes duplicates and only unique items will be reserved.
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
print('lst: ', lst)
st = set(lst)  # the order is random, because sets in general are unordered
print('st: ', st)
lst = list(st)
print('lst: ', lst)

# ------ Joining Sets ------

# We can join two sets using the union() or update() method.
# Union method returns a new set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('fruits: ', fruits)
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print('vegetables: ', vegetables)
fruit_and_veg = fruits.union(vegetables)
print('fruit_and_veg: ', fruit_and_veg)

# Update method inserts a set into a given set
fruits.update(vegetables)
print('fruits: ', fruits)

# ------ Finding Intersection Items ------

# Intersection returns a set of items which are in both sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('whole_numbers: ', whole_numbers)
even_numbers = {0, 2, 4, 6, 8, 10}
print('even_numbers: ', even_numbers)
intersect = whole_numbers.intersection(even_numbers)  # {0, 2, 4, 6, 8, 10}
print('intersect: ', intersect)

python = {'p', 'y', 't', 'h', 'o', 'n'}
print('python: ', python)
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print('dragon: ', dragon)
intersect = python.intersection(dragon)     # {'o', 'n'}
print('intersect: ', intersect)

# ------ Checking Super Set And Subset ------

# A set can be a subset or super set of other sets:
# Subset: issubset()
# Super set: issuperset
print('whole_numbers: ', whole_numbers)
print('even_numbers: ', even_numbers)
is_subset = whole_numbers.issubset(even_numbers) # False, because it is a super set
print('Is whole_numbers a subset of even_numbers?: ', is_subset)
is_super_set = whole_numbers.issuperset(even_numbers) # True
print('Is whole_numbers a super set of even_numbers?: ', is_super_set)

# ------ Checking Difference Between 2 Sets ------

# It returns the difference between two sets.
odd_numbers = whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
print('odd_numbers: ', odd_numbers)

diff = python.difference(dragon)     # {'p', 'y', 't', 'h'}  - the result is unordered (characteristic of sets)
print('python.difference(dragon): ', diff)
diff = dragon.difference(python)     # {'d', 'r', 'a', 'g'}
print('dragon.difference(python): ', diff)

# ------ Finding Symmetric Difference Between 2 Sets ------

# Returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
some_numbers = {1, 2, 3, 4, 5}
print('whole_numbers: ', whole_numbers)
print('some_numbers: ', some_numbers)
sym_diff = whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}
print('Symmetric Difference between whole_numbers and some_numbers: ', sym_diff)

sym_diff = python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
print('Symmetric Difference between python and dragon: ', sym_diff)

# ------ Joining Sets ------

# If two sets do not have a common item or items we call them disjoint sets.
# We can check if two sets are joint or disjoint using isdisjoint() method.
joint = even_numbers.isdisjoint(odd_numbers) # True, because no common item
print('Are even_numbers and odd_numbers disjoint sets?: ', joint)

joint = python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
print('Are python and dragon disjoint sets?: ', joint)

# ------ Exercises 1 ------

# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1: Find the length of the set it_companies
print('1: ')
print('it_companies: ', it_companies)
print('Length of it_companies: ', len(it_companies))

# 2: Add 'Twitter' to it_companies
print('2: ')
it_companies.add('Twitter')
print('it_companies: ', it_companies)

# 3: Insert multiple IT companies at once to the set it_companies
print('3: ')
it_companies.update(['Meta', 'Nvidia', 'AMD'])
print('it_companies: ', it_companies)

# 4: Remove one of the companies from the set it_companies
print('4: ')
it_companies.remove('Facebook')
print('it_companies: ', it_companies)

# 5: What is the difference between remove and discard
print('5: ')
print('remove returns an error if the item is not found in the set, discard does not')

# ------ Exercises 2 ------

# 1: Join A and B
print('1: ')
joined = A.union(B)
print('A: ', A)
print('B: ', B)
print('joined: ', joined)

# 2: Find A intersection B
print('2: ')
intersect = A.intersection(B)
print('A intersection B: ', intersect)

# 3: Is A subset of B
print('3: ')
subset = A.issubset(B)
print('Is A a subset of B?: ', subset)

# 4: Are A and B disjoint sets
print('4: ')
joint = A.isdisjoint(B)
print('Are A and B disjoint sets?: ', joint)

# 5: Join A with B and B with A
print('5: ')
A_join_B = A.union(B)
B_join_A = B.union(A)
print('A_join_B: ', A_join_B)
print('B_join_A: ', B_join_A)

# 6: What is the symmetric difference between A and B
print('6: ')
sym_diff = A.symmetric_difference(B)
print('Symmetric difference between A and B?: ', sym_diff)

# 7: Delete the sets completely
print('7: ')
del A, B

# ------ Exercises 3 ------

# 1: Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print('1: ')
print('age list: ', age)
length_list = len(age)
print('Length of age list: ', length_list)
age_set = set(age)
print('age set: ', age_set)
length_set = len(age_set)
print('Length of age set: ', length_set)
if length_set > length_list :
    print('The set is longer than the list')
elif length_list > length_set :
    print('The list is longer than the set')
else :
    print('They are the same length')

# 2: Explain the difference between the following data types: string, list, tuple and set
print('2: ')
print('Strings: immutable sequences of characters')
print('Lists: mutable ordered collections')
print('Tuples: immutable ordered collections')
print('Sets: mutable unordered collections that store only unique elements')

# 3: I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
print('3: ')
statement = 'I am a teacher and I love to inspire and teach people.'
statement_split = statement.split()
unique_words = []
counter = 0
for i in statement_split :
    if i not in unique_words :
        unique_words.append(i)
        counter += 1
print(counter, unique_words)
unique_words = set(unique_words)
print('No. of Unique Words: ', len(unique_words))

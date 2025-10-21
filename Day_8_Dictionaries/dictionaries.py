# ------ Dictionaries ------
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# The dictionary values could be any data types: string, boolean, list, tuple, set or a dictionary.

# ------ Creating a Dictionary ------

# To create a dictionary we use curly brackets, {} or the dict() built-in function.
empty_dict = {}
print('empty_dict: ', empty_dict)

person = {
    'first_name': 'Adam',
    'last_name': 'Strahan',
    'age': 28,
    'country': 'Ireland',
    'is_married': False,
    'skills': ['JavaScript', 'Java', 'SQL', 'HTML', 'Python'],
    'address': {
        'street': 'Easy Street',
        'zipcode': '90210'
    }
    }
print('person: ', person)
print('Length of person: ', len(person))

# ------ Accessing Dictionary Items ------

# Use the key to access value
print(person['first_name']) # Adam
print(person['country'])    # Ireland
print(person['skills'])     # ['JavaScript', 'Java', 'SQL', 'HTML', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Easy Street
#print(person['city'])        Error

# Accessing an item by key name raises an error if the key does not exist.
# To avoid this error first we have to check if a key exists or we can use the get method.
# The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('first_name')) # Adam
print(person.get('country'))    # Ireland
print(person.get('skills'))     # ['JavaScript', 'Java', 'SQL', 'HTML', 'Python']
print(person.get('skills')[0])  # JavaScript
print(person.get('address')['street'])  # Easy Street
print(person.get('city'))       # None

# ------ Adding Items to Dictionary ------

person['job_title'] = 'Developer'
person['skills'].append('CSS')
print('person: ', person)

# ------ Modifying Items In A Dictionary ------

person['first_name'] = 'Hagrid'
person['age'] = 252
print('person: ', person)

# ------ Checking Keys In A Dictionary ------

# We use the in operator to check if a key exists in a dictionary
print('Age in person?: ', 'age' in person)  # True
print('Size in person?: ', 'size' in person)  # False

# ------ Removing Key And Value Pairs From A Dictionary ------

# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name
person.pop('first_name')        # Removes the firstname item
print('person: ', person)
person.popitem()                # Removes the address item
print('person: ', person)
del person['is_married']        # Removes the is_married item
print('person: ', person)

# ------ Changing A Dictionary To A List Of Items ------

# The items() method changes dictionary to a list of tuples.
print('person as List of Tuples: ', person.items())

# ------ Clearing A Dictionary ------

print('Cleared person: ', person.clear())

# ------ Deleting A Dictionary ------

del person
#print(person)  Error

# ------ Copy A Dictionary ------

# We can copy a dictionary using a copy() method.
# Using copy we can avoid mutation of the original dictionary.
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('dct: ', dct)
print('dct_copy: ', dct_copy)
dct_copy['key5'] = 'value5'
print('dct: ', dct)
print('dct_copy: ', dct_copy)

# ------ Getting Dictionary Keys As A List ------

# The keys() method gives us all the keys of a a dictionary as a list.
keys = dct.keys()
print('dct keys: ', keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# ------ Getting Dictionary Values As A List ------

# The values() method gives us all the values of a a dictionary as a list.
values = dct.values()
print('dct values: ', values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

# ------ Exercises ------

# 1: Create an empty dictionary called dog
print('1: ')
dog = dict()
print('dog: ', dog)

# 2: Add name, color, breed, legs, age to the dog dictionary
print('2: ')
dog['name'] = 'Rocket'
dog['color'] = 'Grey'
dog['breed'] = 'Pug'
dog['legs'] = 4
dog['age'] = 4
print('dog: ', dog)

# 3: Create a student dictionary and add first_name, last_name, gender, age, marital_status,
# skills, country, city and address as keys for the dictionary
print('3: ')
student = {
    'first_name': 'James',
    'last_name': 'Bond',
    'gender': 'Male',
    'age': 50,
    'marital_status': 'Single',
    'skills': ['Spying', 'Shooting', 'Drinking'],
    'country': 'England',
    'city': 'London',
    'address': {
        'street': 'Bond Street',
        'zipcode': '007'
    }
}
print('student: ', student)

# 4: Get the length of the student dictionary
print('4: ')
print('Length of student: ', len(student))

# 5: Get the value of skills and check the data type, it should be a list
print('5: ')
print('Skills: ', student.get('skills'))
print('Skills Type: ', type(student.get('skills')))

# 6: Modify the skills values by adding one or two skills
print('6: ')
student['skills'].append('Smooth Talking')
student['skills'].append('Driving')
print('Skills: ', student['skills'])

# 7: Get the dictionary keys as a list
print('7: ')
print('Student Keys: ', student.keys())

# 8: Get the dictionary values as a list
print('8: ')
print('Student Values: ', student.values())

# 9: Change the dictionary to a list of tuples using items() method
print('9: ')
student_list = student.items()
print('Student as list of tuples: ', student_list)

# 10: Delete one of the items in the dictionary
print('10: ')
student.pop('marital_status')
print('Marital Status Removed: ', student)

# 11: Delete one of the dictionaries
print('11: ')
del student
#print(student)
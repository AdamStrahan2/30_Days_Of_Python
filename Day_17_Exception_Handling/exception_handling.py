# ------ Exception Handling ------

# Python uses try and except to handle errors gracefully.
# A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a
# serious error condition and exits gracefully, in a controlled manner as a result.
# Often the program prints a descriptive error message to a terminal or log as part of the graceful exit.
# An example of exceptions could be an incorrect input, wrong file name, unable to find a file,
# a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.
# If we use try and except in our program, then it will not raise errors in those blocks.
from datetime import datetime

try:
    print(10 + '5')
except:
    print('Something went wrong!')

# Example with TypeError
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    now = datetime.now()
    current_year = now.year
    age = current_year - year_born
    print(f'You are {name} and your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('zero division error occurred')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')

# Fixed TypeError
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    now = datetime.now()
    current_year = now.year
    age = int(current_year) - int(year_born)
    print(f'You are {name} and your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block.')
finally:
    print('I always run.')

# Code Shortened with TypeError to show exception
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    now = datetime.now()
    current_year = now.year
    age = current_year - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)  # unsupported operand type(s) for -: 'int' and 'str'

# ------ Packing/Unpacking Arguments in Python ------

# We use two operators:
#   * for tuples
#   ** for dictionaries
# Look at the example below. It takes only arguments but we have list.
# We can unpack the list and change to arguments.

# ------ Unpacking Lists ------

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
#print(sum_of_five_nums(lst))  # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

print('sum_of_five_nums:', sum_of_five_nums(*lst))  # 15

# We can also use unpacking in the range built-in function that expects a start and an end.
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)          # range(2, 7)
print(list(numbers))    # [2, 3, 4, 5, 6]

# A list or a tuple can also be unpacked like this:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)    # 1 [2, 3, 4, 5, 6] 7

# ------ Unpacking Dictionaries ------

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {city}, {country}. He is {age} years old.'

dct = {'name':'Adam', 'country':'Ireland', 'city':'Carlow', 'age':28}
print(unpacking_person_info(**dct))  # Adam lives in Carlow, Ireland. He is 28 years old.

# ------ Packing Lists ------

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 2, 3))              # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28

# ------ Packing Dictionaries ------

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Adam", country="Ireland", city="Carlow", age=28))

# ------ Spreading in Python ------

# Like in JavaScript, spreading is possible in Python.
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print('lst:', lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print('nordic_countries:', nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# ------ Enumerate ------

# If we want an index of a list, we use enumerate built-in function to get the index of each item in the list.
for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(nordic_countries):
    print(f'nordic_countries for loop x{index}')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
    if i == 'Germany':
        print(f'The country {i} has been found at index {index}')
    if i == 'Denmark':
        print(f'The country {i} has been found at index {index}')

# ------ Zip ------

# Sometimes we would like to combine lists when looping through them.
fruit = ['banana', 'orange', 'mango', 'lemon', 'lime']
veg = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruit_and_veg = []
for f, v in zip(fruit, veg):
    fruit_and_veg.append({'fruit': f, 'veg': v})

print(fruit_and_veg)  # [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]

# ------ Exercises ------

names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# 1: Unpack the first five countries and store them in a variable nordic_countries,
#    store Estonia and Russia in es, and ru respectively.
print('1:')
*nordic_countries, es, ru = names
print('nordic_countries:', nordic_countries)
print('es:', es)
print('ru:', ru)

# ------ Higher Order Functions ------

# In Python functions are treated as 1st class citizens, allowing you to perform the following operations on functions:
# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# ------ Function As A Parameter ------

def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# ------ Function As A Return Value ------

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# ------ Python Closures ------

# Python allows a nested function to access the outer scope of the enclosing function.
# This is known as a Closure. In Python, closure is created by nesting a function inside
# another encapsulating function and then returning the inner function.
def add_ten():
    ten = 10
    def add(num):
        return num + ten  # ten can be accessed inside add() through Closure
    return add  # return the inner function

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# ------ Python Decorators ------

# A decorator is a design pattern in Python that allows a user to add new functionality to an
# existing object without modifying its structure. Decorators are usually called before the
# definition of a function you want to decorate.

# ------ Creating Decorators ------

# To create a decorator function, we need an outer function with an inner wrapper function.
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

# This decorator function is a higher order function that takes a function as a parameter
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# ------ Applying Multiple Decorators To A Function ------

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator  # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

# ------ Accepting Parameters In Decorator Functions ------

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to learn.".format(
        first_name, last_name, country))

print_full_name('Adam', 'Strahan', 'Ireland')

# ------ Built-in Higher Order Functions ------

# Some of the built-in higher order functions are map(), filter, and reduce. Lambda function can be passed
# as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

# ------ Map Function ------

# The map() function is a built-in function that takes a function and iterable as parameters.
# Example  1
numbers = [1, 2, 3, 4, 5]  # iterable
def square(x):             # function
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Apply it with a lambda function
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Example 2
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

# Example 3
names = ['Adam', 'Daniel', 'John', 'Patrick']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ADAM', 'DANIEL', 'JOHN', 'PATRICK']

# Apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ADAM', 'DANIEL', 'JOHN', 'PATRICK']

# ------ Filter Function ------

# The filter() function calls the specified function which returns boolean for each item of the specified
# iterable (list). It filters the items that satisfy the filtering criteria.
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# Filter long name
names = ['Adam', 'LeShawn', 'Jack', 'Mohammad']  # iterable
def is_name_long(name):
    if len(name) >= 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['LeShawn', 'Mohammad']

# ------ Reduce Function ------

# The reduce() function is defined in the functools module and we should import it from this module.
# Like map and filter it takes two parameters, a function and an iterable.
# However, it does not return another iterable, instead it returns a single value.
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print('total:', total)    # 15

# ------ Exercises 1 ------

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Adam', 'Daniel', 'John', 'Patrick']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1: Explain the difference between map, filter, and reduce.
print('1:')
print('Map: Apply a function to every item in an iterable (like a list) and return a new iterable with the results.')
print('Filter: Keep only the elements that satisfy a certain condition (where the function returns True).')
print('Reduce: Repeatedly apply a function to the elements, reducing the iterable to a single value.')

# 2: Explain the difference between higher order function, closure and decorator
print('2:')
print('Higher Order Function: A function that takes another function as an argument or returns a function.')
print('Closure: A function that remembers variables from its enclosing scope even after that scope is finished.')
print('Decorator: A higher order function, adds new behaviour and returns a new function without modifying old one.')

# 3: Define a call function before map, filter or reduce.
print('3:')
def double(x):
    return x * 2

print('numbers:', numbers)
doubled_nums = list(map(double, numbers))
print('doubled_nums:', doubled_nums)

# 4: Use for loop to print each country in the countries list.
print('4:')
for country in countries:
    print(country)

# 5: Use for to print each name in the names list.
print('5:')
for name in names:
    print(name)

# 6: Use for to print each number in the numbers list.
print('6:')
for num in numbers:
    print(num)

# ------ Exercises 2 ------

# 1: Use map to create a new list by changing each country to uppercase in the countries list.
print('1:')
def uppercase(lst):
    return lst.upper()

upper_country_list = map(uppercase, countries)
print('upper_country_list:', list(upper_country_list))

# 2: Use map to create a new list by changing each number to its square in the numbers list
print('2:')
def square(x):
    return x ** 2

print('numbers:', numbers)
squared_list = map(square, numbers)
print('squared_list:', list(squared_list))

# 3: Use map to change each name to uppercase in the names list
print('3:')
def uppercase(lst):
    return lst.upper()

upper_names = map(uppercase, names)
print('upper_names:', list(upper_names))

# 4: Use filter to filter out countries containing 'land'.
print('4:')
land_countries = list(filter(lambda country: 'land' in country.lower(), countries))
print('countries:', countries)
print('land_countries:', land_countries)

# 5: Use filter to filter out countries having exactly six characters.
print('5:')
def countries_6_letters(country):
    if len(country) == 6:
        return True
    else:
        return False

six_letter_countries = list(filter(countries_6_letters, countries))
print('six_letter_countries:', six_letter_countries)

# 6: Use filter to filter out countries containing six letters and more in the country list.
print('6:')
def countries_6_plus_letters(country):
    if len(country) >= 6:
        return True
    else:
        return False

six_plus_letter_countries = list(filter(countries_6_plus_letters, countries))
print('six_plus_letter_countries:', six_plus_letter_countries)

# 7: Use filter to filter out countries starting with an 'E'
print('7:')
e_countries = list(filter(lambda country: country.lower().startswith('e'), countries))
print('e_countries:', e_countries)

# 8: Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print('8:')
print('numbers:', numbers)
result = reduce(
    lambda acc, x: acc + x,  # 3) Reduce numbers by adding them together
    filter(
        lambda x: x % 2 == 0,  # 2) Filter for even numbers
        map(lambda x: x * 2, numbers)  # 1) Doubles each number in the list
    )
)
print('Result:', result)

# 9: Declare a function called get_string_lists which takes a list as a parameter and then returns
# a list containing only string items.
print('9:')
mixed_list = ['Python', 10, True, 'Java', [1, 2], 'C++']
print('mixed_list:', mixed_list)
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

string_list = get_string_lists(mixed_list)
print('string_list:', string_list)

# 10: Use reduce to sum all the numbers in the numbers list.
print('10:')
def add_nums(x, y):
    return int(x) + int(y)

result = reduce(add_nums, numbers)
print('result:', result)

# 11: Use reduce to concatenate all the countries and to produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway and Iceland are north European countries
print('11:')
sentence = reduce(
    lambda acc, country: f'{acc}, {country}' if country != countries[-1] else f'{acc} and {country}',
    countries[1:],
    countries[0]
) + ' are north European countries.'
print(sentence)

# 12: Declare a function called categorize_countries that returns a list of countries with some common
# pattern (you can find the countries list in this repository as countries.py(eg 'land', 'ia', 'island', 'stan')).
print('12:')
from data.countries import countries as country_list
def categorize_countries(pattern):
    return [country for country in country_list if pattern.lower() in country.lower()]

print('country_list:', country_list)
print('stan:', categorize_countries('stan'))
print('land:', categorize_countries('land'))
print('ia:', categorize_countries('ia'))

# 13: Create a function returning a dictionary, where keys stand for starting letters of countries and
# values are the number of country names starting with that letter.
print('13:')
def count_countries_by_letter():
    return {
        letter: sum(country.startswith(letter) for country in country_list)  # Counts number of countries starting with each letter
        for letter in sorted({country[0].upper() for country in country_list})  # Creates a set of unique first letters
    }

print('count_countries_by_letter:', count_countries_by_letter())

# 14: Declare a get_first_ten_countries function - it returns a list of first ten countries
# from the countries.py list in the data folder.
print('14:')
def get_first_ten_countries():
    return country_list[:10]

print('get_first_ten_countries:', get_first_ten_countries())

# 15: Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print('15:')
def get_last_ten_countries():
    return country_list[-10:]

print('get_last_ten_countries:', get_last_ten_countries())

# ------ Exercises 3 ------

# 1: Use the countries_data.py file and follow the tasks:
from data.countries_data import countries_info

# A: Sort countries by name, by capital, by population
print('1A:')
def sort_by_name(data):
    return sorted(data, key=lambda x: x['name'])

def sort_by_capital(data):
    return sorted(data, key=lambda x: x['capital'])

def sort_by_population(data):
    return sorted(data, key=lambda x: x['population'], reverse=True)

print('Sort by Name:')
for c in sort_by_name(countries_info):
    print(c)

print('Sort by Capital:')
for c in sort_by_capital(countries_info):
    print(c)

print('Sort by Population:')
for c in sort_by_population(countries_info):
    print(c)

# 1B: Sort out the ten most spoken languages by location.
from collections import Counter
print('1B:')
def most_spoken_languages(n=10):
    all_languages = [lang for country in countries_info for lang in country['languages']]
    language_counts = Counter(all_languages)
    return language_counts.most_common(n)

print('10 Most Spoken Languages:', most_spoken_languages())

# 1C: Sort out the ten most populated countries.
print('1C:')
def most_populated_countries(n=10):
    sorted_countries = sorted(countries_info, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:n]

for c in most_populated_countries(10):
    print(f"{c['name']}: {c['population']}")

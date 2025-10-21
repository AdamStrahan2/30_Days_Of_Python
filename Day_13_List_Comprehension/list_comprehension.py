# ------ List Comprehension ------

# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to
# create a new list. List comprehension is considerably faster than processing a list using the for loop.
# One way
language = 'Python'
lst = list(language)  # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))  # list
print(lst)        # ['P', 'y', 't', 'h', 'o', 'n']

# ------ For Loop ------

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print('numbers:', numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print('squares:', squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print('numbers:', numbers)

# ------ If Statements ------

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print('even_numbers:', even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print('odd_numbers:', odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print('positive_even_numbers:', positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print('list_of_lists:', list_of_lists)
print('Flattened 3D Array:', flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ------ Lambda Function ------

# Lambda function is a small anonymous function without a name. It can take any number of arguments,
# but can only have one expression. Lambda function is similar to anonymous functions in JavaScript.
# We need it when we want to write an anonymous function inside another function.

# ------ Creating a Lambda Function ------

# To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression.
# Lambda function does not use return but it explicitly returns the expression.
# Named function
def add_two_nums(a, b):
    return a + b

print('add_two_nums:', add_two_nums(2, 3))     # 5

# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print('Lambda add_two_nums:', add_two_nums(2, 3))    # 5

# Self invoking lambda function
print('Self invoking function:', (lambda a, b: a + b)(2, 3))  # 5

square = lambda x: x ** 2
print('square:', square(3))    # 9
cube = lambda x: x ** 3
print('cube:', cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print('multiple_variable:', multiple_variable(5, 5, 3))  # 22

# ------ Lambda Function Inside Another Function ------

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print('cube:', cube)          # 8
two_power_of_five = power(2)(5)
print('two_power_of_five:', two_power_of_five)  # 32

# ------ Exercises ------

# 1: Filter only negative and zero in the list using list comprehension
print('1:')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i < 1]
print('negative_and_zero:', negative_and_zero)

# 2: Flatten the following list of lists of lists to a one dimensional list
print('2:')
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [number for row in list_of_lists for inner in row for number in inner]
# for row in list_of_lists → goes over [[1,2,3]], [[4,5,6]], [[7,8,9]]
# for inner in row → goes over [1,2,3], [4,5,6], [7,8,9]
# for num in inner → picks the numbers inside each of those lists.
print('flattened:', flattened)

# 3: Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
print('3:')
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print('list_of_tuples:', list_of_tuples)

# 4: Flatten the following list to a new list:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
print('4:')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), capital.upper()]
          for sublist in countries  # iterates through [[('Finland', 'Helsinki')]], etc.
          for (country, capital) in sublist]  # unpacks the tuple ('Finland', 'Helsinki')
print('output:', output)

# 5: Change the following list to a list of dictionaries:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
print('5:')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country': country.upper(), 'city': capital.upper()}
          for sublist in countries
          for (country, capital) in sublist]
print('output:', output)

# 6: Change the following list of lists to a list of concatenated strings:
# output: ['Adam Strahan', 'David Smith', 'Bernie Sanders', 'Bill Gates']
print('6:')
names = [[('Adam', 'Strahan')], [('David', 'Smith')], [('Bernie', 'Sanders')], [('Bill', 'Gates')]]
output = [f'{first} {last}'
          for sublist in names
          for (first, last) in sublist]
print('output:', output)

# 7: Write a lambda function which can solve a slope or y-intercept of linear functions.
print('7:')
linear_params = lambda x1, y1, x2, y2: (
    # get the slope
    (y2 - y1) / (x2 - x1),
    # get the y intercept
    y1 - ((y2 - y1) / (x2 - x1)) * x1
)
m, c = linear_params(2, 4, 6, 12)
print("slope:", m)
print("y-intercept:", c)

import math
import keyword
from Data.countries_data import countries_info
from collections import Counter
# ------ Functions ------
# A function is a reusable block of code or programming statements designed to perform a certain task.
# To define or declare a function, Python provides the def keyword.
# The function block of code is executed only if the function is called or invoked.

# ------ Declaring and Calling Functions ------

# ------ Function Without Parameters ------
def generate_full_name():
    first_name = 'Adam'
    last_name = 'Strahan'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
    # Leave 2 blank lines after function code


generate_full_name()  # calling a function


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()

# ------ Function Returning A Value 1 ------

def generate_full_name():
    first_name = 'Adam'
    last_name = 'Strahan'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())

# ------ Functions With Parameters ------

# In a function we can pass different data types
# (number, string, boolean, list, tuple, dictionary or set) as a parameter

# Single Parameter
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings('Adam'))


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90))


def square_number(x):
    return x * x


print(square_number(2))


def area_of_circle (r):
    pi = 3.14
    area = pi * r ** 2
    return area


print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)


sum_of_numbers(10)  # 55
sum_of_numbers(100)  # 5050

# 2 Parameters
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print('Full Name: ', generate_full_name('Adam', 'Strahan'))


def sum_two_numbers(num_one, num_two):
    total = num_one + num_two
    return total


print('Sum of two numbers: ', sum_two_numbers(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(2025, 1997))


def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N'  # the value has to be changed to a string first
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# ------ Passing Arguments With Key And Value ------

# If we pass the arguments with key and value, the order of the arguments does not matter.
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)


print_fullname(firstname='Adam', lastname='Strahan')


def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)


add_two_numbers(3, 2)  # Order does not matter

# ------ Function Returning A Value 2 ------

# If we do not return a value with a function, then our function is returning None by default.
# To return a value with a function we use the keyword return followed by the variable we are returning.
# We can return any kind of data types from a function.

# Returning a String
def print_name(firstname):
    return firstname


print(print_name('Adam'))  # Adam


def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name


print(print_full_name(firstname='Adam', lastname='Strahan'))  # Adam Strahan

# Returning a Number
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(2025, 1997))

# Returning a Boolean
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break
    return False


print(is_even(10))  # True
print(is_even(7))  # False

# Returning a List
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))

# ------ Function With Default Parameters ------

def greetings(name = 'Peter'):  # Setting default value to Peter
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings())  # Default value Peter used
print(greetings('Adam'))


def generate_full_name(first_name='Adam', last_name='Strahan'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
print(generate_full_name('David', 'Smith'))


def calculate_age(birth_year, current_year=2025):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(1997))


def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity) + ' N'  # the value has to be changed to string first
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100))  # 9.81 - average gravity on Earth
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))  # gravity on the Moon

# ------ Arbitrary Number Of Arguments ------

# If we do not know the number of arguments we pass to our function, we can create a function which can
# take arbitrary number of arguments by adding * before the parameter name.
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num
    return total


print(sum_all_nums(2, 3))  # 5
print(sum_all_nums(2, 3, 5))  # 10
print(sum_all_nums(2, 3, 5, 7))  # 17
print(sum_all_nums(2, 3, 5, 10, 10, 10, 10, 10, 10, 10))  # 80

# ------ Default And Arbitrary Number Of Parameters In Function ------

def generate_groups (team, *args):
    print('Team: ', team)
    for i in args:
        print('Member: ', i)


generate_groups('Team Rocket', 'Adam', 'Sine', 'Callum', 'Nathan', 'Paula')

# ------ Function As A Parameter Of Another Function ------

#You can pass functions around as parameters
def square_number(n):
    print('n: ', n)  # n:  3
    print('n * n: ', n * n)  # n * n:  9
    return n * n


def do_something(f, x):
    print('f: ', f)  # <function square_number at 0x0000021625229D00>
    print('x: ', x)  # x:  3
    print('f(x): ', f(x))  # f(x):  9
    return f(x)


print(do_something(square_number, 3))  # 9

# ------ Exercises 1 ------

# 1: Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print('1: ')
def add_two_numbers(num1, num2):
    return num1 + num2

print('add_two_numbers:', add_two_numbers(10, 12))

# 2: Area of a circle is calculated as follows: area = π x r x r.
# Write a function that calculates area_of_circle.
print('2: ')
def calculate_circle_area(radius):
    pi = 3.14
    return pi * radius * radius

print('calculate_circle_area:', calculate_circle_area(10))

# 3: Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
print('3: ')
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print('add_all_nums:', add_all_nums(1, 2, 3, 4, 5, 6))

# 4: Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
print('4: ')
def convert_celsius_to_fahrenheit(cel):
    fahr = (cel * 9/5) + 32
    return fahr

print('convert_celsius_to_fahrenheit:', convert_celsius_to_fahrenheit(20))

# 5: Write a function called check_season, it takes a month parameter and returns: Autumn, Winter, Spring or Summer.
print('5: ')
def check_season(month):
    season = ''
    if month == 'February' or month == 'March' or month == 'April':
        season = 'Spring'
        return season
    elif month == 'May' or month == 'June' or month == 'July':
        season = 'Summer'
        return season
    elif month == 'August' or month == 'September' or month == 'October':
        season = 'Autumn'
        return season
    elif month == 'November' or month == 'December' or month == 'January':
        season = 'Winter'
        return season
    else:
        season = 'Invalid Month'
        return season

print('check_season:', check_season('September'))

# 6: Write a function called calculate_slope which return the slope of a linear equation
print('6: ')
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return str('Vertical Line')  # Handle vertical line
    return (y2 - y1) / (x2 - x1)

print('calculate_slope:', calculate_slope(2, 4, 3, 6))
print('calculate_slope:', calculate_slope(3, 4, 3, 6))

# 7: Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print('7: ')
def solve_quadratic_eqn(a, b, c):
    # Return the solution set of a quadratic equation ax² + bx + c = 0.
    if a == 0:
        # Handle the case where it's not a quadratic equation
        if b == 0:
            return "No solution" if c != 0 else "Infinite solutions"
        return [-c / b]  # Linear equation solution

    discriminant = b ** 2 - 4 * a * c

    # The discriminant 𝐷 = b ** 2 - 4ac determines the type of roots:
    # D > 0 → two distinct real roots
    # D = 0 → one real repeated root
    # D<0 → two complex conjugate roots
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        # For complex (non-real) roots
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        return [complex(real_part, imag_part), complex(real_part, -imag_part)]

print('solve_quadratic_eqn:', solve_quadratic_eqn(1, -3, 2))  # [2.0, 1.0]
print('solve_quadratic_eqn:', solve_quadratic_eqn(1, 2, 1))  # [-1.0]
print('solve_quadratic_eqn:', solve_quadratic_eqn(1, 1, 1))  # [(-0.5+0.866j), (-0.5-0.866j)]

# 8: Declare a function named print_list.
# It takes a list as a parameter and it prints out each element of the list.
print('8: ')
lst = ['much', 'ado', 'about', 'nothing']
def print_list(lst):
    for item in lst:
        print(item)

print_list(lst)

# 9: Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops).
print('9: ')
numbers = [1, 2, 3, 4, 5]
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  # Start from last index down to 0
        reversed_arr.append(arr[i])
    return reversed_arr

print('reverse_list:', reverse_list(numbers))  # [5, 4, 3, 2, 1]

# 10: Declare a function named capitalize_list_items. It takes a list as a parameter
# and it returns a capitalized list of items
print('10: ')
lst = ['john', 'bob', 'jackie', 'mary']
def capitalize_list_items(lst):
    cap_lst = []
    for name in lst:
        cap_lst.append(name.capitalize())
    return cap_lst

print('capitalize_list_items:', capitalize_list_items(lst))

# 11: Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
print('11: ')
numbers = [1, 2, 3, 4, 5]
def add_item(lst, item):
    lst.append(item)
    return lst

print('add_item:', add_item(numbers, 6))

# 12: Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
print('12: ')
fruit = ['apple', 'pear', 'orange', 'banana', 'milk']
def remove_item(lst, item):
    lst.remove(item)
    return lst

print('remove_item:', remove_item(fruit, 'milk'))

# 13: Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.
print('13: ')
def sum_of_numbers(num):
    total = 0
    for number in range(num + 1):
        total += number
    return total

print('sum_of_numbers:', sum_of_numbers(100))

# 14: Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print('14: ')
def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            total += i
    return total

print('sum_of_odds:', sum_of_odds(10))  # 25

# 15: Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
print('15: ')
def sum_of_even(num):
    total = 0
    for i in range(0, num + 1):
        if i % 2 == 0:
            total += i
    return total

print('sum_of_even:', sum_of_even(10))  # 30

# ------ Exercises 2 ------

# 1: Declare a function named evens_and_odds.
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
print('1: ')
def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(0, num + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print('The number of odds are', odd_count)  # 50
    print('The number of evens are', even_count)  # 51

evens_and_odds(100)

# 1: Call your function factorial, it takes a whole number as a parameter and it returns a factorial of the number
print('1: ')
# A factorial is the product of a positive integer and all the positive integers below it.
def factorial(num):
    if num < 0:
        return 'Factorial not defined for negative numbers'
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

print('factorial:', factorial(5))  # 120

# 2: Call your function is_empty, it takes a parameter and it checks if it is empty or not
print('2: ')
def is_empty(par):
    if par:
        return False
    else:
        return True

print('is_empty:', is_empty([]))  # True
print('is_empty:', is_empty({}))  # True
print('is_empty:', is_empty(''))  # True
print('is_empty:', is_empty('{}'))  # False
print('is_empty:', is_empty(5))  # False

# 3: Write different functions which take lists. They should calculate_mean, calculate_median,
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print('3: ')
numbers = [4, 7, 2, 9, 7, 3, 7, 5]
vnumbers = [2.25, 2.25, 12.25, 12.25, 2.25, 6.25, 2.25, 0.25]
# Return mean (average) of list numbers
def calculate_mean(data):
    return sum(data) / len(data)

# Return median (middle value) of list numbers
def calculate_median(data):
    sorted_numbers = sorted(data)
    length = len(data)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

# Return mode (most frequent value) of list numbers
def calculate_mode(data):
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_count]
    if len(modes) == len(frequency):
        # No mode, all values occur equally
        return None
    return modes if len(modes) > 1 else modes[0]

# Return range (max - min) of list numbers
def calculate_range(data):
    return max(data) - min(data)

# Return variance of list numbers
def calculate_variance(data):
    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(data)

# Return standard deviation of list of numbers
def calculate_std(data):
    variance = calculate_variance(data)
    return variance ** 0.5

print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard Deviation:", calculate_std(numbers))

# ------ Exercises 3 ------

# 1: Write a function called is_prime, which checks if a number is prime.
print('1: ')
def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    if num == 2:
        return True   # 2 is the only even prime number
    if num % 2 == 0:
        return False  # All other even numbers are not prime

    # Check divisibility from 3 to √n
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

print('7 is_prime:', is_prime(7))
print('2 is_prime:', is_prime(2))
print('19 is_prime:', is_prime(19))
print('25 is_prime:', is_prime(25))

# 2: Write a function which checks if all items are unique in the list.
print('2: ')
def are_items_unique(lst):
    return len(lst) == len(set(lst))

print('are_items_unique:', are_items_unique([1, 2, 3, 4, 5]))      # True
print('are_items_unique:', are_items_unique([1, 2, 2, 3, 4]))      # False
print('are_items_unique:', are_items_unique(['a', 'b', 'c', 'a'])) # False

# 3: Write a function which checks if all the items of the list are of the same data type.
print('3: ')
def all_same_type(lst):
    if not lst:  # empty list
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

print('all_same_type:', all_same_type([1, 2, 3]))        # True
print('all_same_type:', all_same_type([1, "2", 3]))      # False
print('all_same_type:', all_same_type([]))               # True
print('all_same_type:', all_same_type(["a", "b", "c"]))  # True

# 4: Write a function which checks if provided variable is a valid python variable
print('4: ')
def is_valid_variable(variable):
    if not isinstance(variable, str):  # checks variable is a string
        return False
    if not variable:  # empty string
        return False
    if keyword.iskeyword(variable):  # checks if variable is reserved keyword
        return False
    if variable[0].isdigit():  # checks first character is not a number
        return False
    # checks remaining characters are letters, numbers or underscore
    for char in variable:
        if not (char.isalnum() or char == '_'):
            return False
    return True

print('is_valid_variable:', is_valid_variable("my_var"))    # True
print('is_valid_variable:', is_valid_variable("_var123"))   # True
print('is_valid_variable:', is_valid_variable("123var"))    # False
print('is_valid_variable:', is_valid_variable("for"))       # False

# 5A: Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order
print('5A: ')
def most_spoken_languages(num=10):
    all_languages = []
    for country in countries_info:
        all_languages.extend(country.get('languages', []))
    language_counts = Counter(all_languages)
    # return a list of tuples (language, count) sorted in descending order
    return language_counts.most_common(num)

top_10_languages = most_spoken_languages()
print('Top 10 Languages:', top_10_languages)
top_20_languages = most_spoken_languages(20)
print('Top 20 Languages:', top_20_languages)

# 5B: Create a function called the most_populated_countries.
# It should return 10 or 20 most populated countries in descending order.
print('5B: ')
def most_populated_countries(num=10):
    # sort countries by population in descending order
    sorted_countries = sorted(countries_info, key=lambda x: x.get('population', 0), reverse=True)
    # return top countries as a list of dictionaries with name and population
    return [{'country': c['name'], 'population': c['population']} for c in sorted_countries[:num]]

top_10_countries = most_populated_countries()
print('Top 10 Countries:', top_10_countries)
top_20_countries = most_populated_countries(20)
print('Top 20 Countries:', top_20_countries)
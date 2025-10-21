# ------ Importing Modules ------
# Imports should all be at the top pf the file. For this tutorial they'll be at each step.
# main.py file
import mymodule

print(mymodule.generate_full_name('Adam', 'Strahan')) # Adam Strahan

# ------ Importing Functions From Modules ------

from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Adam', 'Strahan'))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(person['first_name'])

# ------ Importing Functions From Modules And Renaming ------

# During importing we can rename the name of the module.
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Adam', 'Strahan'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['first_name'])

# ------ Importing Built-in Modules ------

# Like other programming languages we can also import modules by importing the file/function using the key
# word import. Some of the common built-in modules: math, datetime, os,sys, random, statistics, collections, json,re

# ------ OS Module ------

# Using python OS module it is possible to automatically perform many operating system tasks.
# The OS module in Python provides functions for creating, changing current working directory,
# and removing a directory (folder), fetching its contents, changing and identifying the current directory.
# import the module
import os
run_os_functions = False
if run_os_functions:
    # Creating a directory
    os.mkdir('directory_name')
    # Changing the current directory
    os.chdir('path')
    # Getting current working directory
    os.getcwd()
    # Removing directory
    os.rmdir('directory_name')

# ------ Sys Module ------

# The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
# Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0
# in this list is always the name of the script, at index 1 is the argument passed from the command line.
import sys
run_sys_functions = False
if run_sys_functions:
    # print(sys.argv[0], sys.argv[1], sys.argv[2])  # this line would print out: filename argument1 argument2
    print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

    # Now to check how this script works I wrote in command line:
    # python main.py Adam 30DaysOfPython

    # The result:
    # Welcome Adam. Enjoy  30DayOfPython challenge!

    # to exit sys
    sys.exit()
    # To know the largest integer variable it takes
    sys.maxsize
    # To know environment path
    sys.path
    # To know the version of python you are using
    sys.version

# ------ Statistics Module ------

# The statistics module provides functions for mathematical statistics of numeric data.
# The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.
from statistics import *  # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(ages)
print('Mean:', mean(ages))       # ~21.09
print('Median:', median(ages))     # 22
print('Mode:', mode(ages))       # 20
print('Standard Deviation:', stdev(ages))      # 6.1

# ------ Math Module ------

# Module containing many mathematical operations and constants.
import math
print('Pi:', math.pi)           # 3.141592653589793, pi constant
print('Square Root:', math.sqrt(2))      # 1.4142135623730951, square root
print('Exponential:', math.pow(2, 3))    # 8.0, exponential function
print('Floor:', math.floor(9.81))  # 9, rounding to the lowest
print('Ceiling:', math.ceil(9.81))   # 10, rounding to the highest
print('Log:', math.log10(100))   # 2, logarithm with 10 as base

# When we import we can also rename the name of the function.
from math import pi as PI
print('PI:', PI)  # 3.141592653589793

# ------ String Module ------

# A string module is a useful module for many purposes.
# The example below shows some use of the string module.
import string
print('Ascii Letters:', string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print('Digits:', string.digits)        # 0123456789
print('Punctuation:', string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# ------ Random Module ------

# module which gives us a random number between 0 and 0.9999.
# The random module has lots of functions but in this section we will only use random and randint.
from random import random, randint
print('Random between 0-0.9999:', random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print('Random in range:', randint(5, 20))  # returns a random integer number between [5, 20] inclusive

# ------ Exercises 1 ------

# 1: Write a function which generates a six digit/character random_user_id.
print('1:')
from random import choice
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(choice(characters) for _ in range(6))

print('Random User ID:', random_user_id())
print('Random User ID:', random_user_id())

# 2: Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is
# the number of characters and the second input is the number of IDs which are supposed to be generated.
print('2:')
def user_id_gen_by_user():
    num_chars = int(input('Enter number of characters per ID: '))
    num_ids = int(input('Enter number of IDs: '))
    characters = string.ascii_letters + string.digits
    for _ in range(num_ids):
        user_id = ''.join(choice(characters) for _ in range(num_chars))
        print('user_id:', user_id)

user_id_gen_by_user()

# 3: Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print('3:')
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f'rgb({r}, {g}, {b})'

print(rgb_color_gen())
print(rgb_color_gen())

# ------ Exercises 2 ------

# 1: Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and
# first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
print('1:')
def list_of_hexa_colors(number):
    colors = []
    for _ in range(number):
        hex_color = '#' + ''.join(choice('0123456789abcdef') for _ in range(6))
        colors.append(hex_color)
    return colors

print('list_of_hexa_colors:', list_of_hexa_colors(5))

# 2: Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print('2:')
def list_of_rgb_colors(number):
    colors = []
    for _ in range(number):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colors.append(f'rgb({r}, {g}, {b})')
    return colors

print('list_of_rgb_colors:', list_of_rgb_colors(8))

# 3: Write a function generate_colors which can generate any number of hexa or rgb colors.
print('3:')
def generate_colors(color_type, number):
    colors = []
    if color_type.lower() == 'hexa':
        for _ in range(number):
            hex_color = '#' + ''.join(choice('0123456789abcdef') for _ in range(6))
            colors.append(hex_color)
    elif color_type.lower() == 'rgb':
        for _ in range(number):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            colors.append(f'rgb({r}, {g}, {b})')
    else:
        return 'Invalid color type! Please use hexa or rgb.'
    return colors

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 5))

# ------ Exercises 3 ------

# 1: Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print('1:')
from random import shuffle
def shuffle_list(lst):
    shuffled_list = lst[:]
    shuffle(shuffled_list)
    return shuffled_list

print('Shuffled List:', shuffle_list([1, 2, 3, 4, 5]))
print('Shuffled List:', shuffle_list(['apple', 'banana', 'cherry', 'date']))

# 2: Write a function which returns an array of seven random numbers in a range of 0-9.
# All the numbers must be unique.
print('2:')
from random import sample
def seven_unique_nums():
    return sample(range(10), 7)

print('7 unique numbers:', seven_unique_nums())

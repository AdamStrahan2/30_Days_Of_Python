# ------ Conditionals ------
# By default, statements in Python script are executed sequentially from top to bottom.
# If the processing logic requires, the sequential flow of execution can be altered in two ways:
# - Conditional execution: a block of one or more statements will be executed if a certain expression is true
# - Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain
# expression is true. In this section, we will cover if, else, elif statements.
# The comparison and logical operators we learned in previous sections will be useful here.

# ------ If Condition ------

# In python and other programming languages the key word if is used to check if a condition is true
# and to execute the block code. Remember the indentation after the colon.
a = 3
if a > 0:
    print('A is a positive number')

# ------ If Else Condition ------

if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# ------ If Elif Else Condition ------

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Short Hand
a = 3
print('A is positive') if a > 0 else print('A is negative')  # first condition met, 'A is positive' will be printed

# ------ Nested Conditions ------

if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# ------ If Condition and Logical Operators ------

a = 4
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# ------ If Condition and Or Logical Operators ------

user = 'James'
access_level = 4
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')

# ------ Exercises 1 ------

# 1: Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
print('1: ')
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
elif age < 0:
    print('Invalid age.')
else:
    rem = 18 - age
    print('You need ', rem, ' more years before you can drive.')

# 2: Compare the values of my_age and your_age using if … else. Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for
# 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
print('2: ')
my_age = 28
your_age = int(input('What age are you?: '))
if your_age == my_age:
    print('We are the same age.')
elif your_age < 0:
    print('Invalid age.')
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print('You are', diff, 'year younger than me.')
    else:
        print('You are', diff, 'years younger than me.')
else:
    diff = your_age - my_age
    if diff == 1:
        print('You are', diff, 'year older than me.')
    else:
        print('You are', diff, 'years older than me.')

# 3: Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b
print('3: ')
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is smaller than', b)
else:
    print(a, 'is equal to', b)

# ------ Exercises 2 ------

# 1: Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
print('1: ')
score = int(input('What is your score?: '))
if score < 0 or score > 100:
    print('Invalid score')
elif score <= 100 and score >= 90:
    print(score, ' Grade: A')
elif score < 90 and score >= 70:
    print(score, ' Grade: B')
elif score < 70 and score >= 60:
    print(score, ' Grade: C')
elif score < 60 and score >= 50:
    print(score, ' Grade: D')
else:
    print(score, ' Grade: F')

# 2 : Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn. December, January or February, the season is Winter.
# March, April or May, the season is Spring. June, July or August, the season is Summer
print('2: ')
month = input('Enter a month: ')
if month == 'March' or month == 'April' or month == 'May':
    print('It is Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('It is Summer')
elif month == 'September' or month == 'October' or month == 'November':
    print('It is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('It is Winter')
else:
    print('Invalid month.')

# 3: If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exists in the list')
print('3: ')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = str(input('Enter a fruit (please use lower case): '))
in_list = new_fruit in fruits
if in_list:
    print('That fruit already exists in the list')
else:
    fruits.append(new_fruit)
    print('fruits: ', fruits)

# ------ Exercises 3 ------

person={
    'first_name': 'Adam',
    'last_name': 'Strahan',
    'age': 28,
    'country': 'Ireland',
    'is_married': False,
    'skills': ['JavaScript', 'Java', 'SQL', 'HTML', 'Python'],
    'address': {
        'street': 'Easy Street',
        'zipcode': '360720'
    }
}

# 1A: Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print('1A: ')
has_key = 'skills' in person
if has_key:
    length = len(person['skills'])
    print('Length of skills list: ', length)
    middle = length // 2
    print('Middle value of skills list: ', person['skills'][middle])
else:
    print('skills key not available')

# 1B: Check if the person dictionary has skills key,
# if so check if the person has 'Python' skill and print out the result.
print('1B: ')
has_key = 'skills' in person
print('Skills exists?: ', has_key)
if has_key:
    has_skill = 'Python' in person['skills']
    if has_skill:
        print('Python exists in skills')
    else:
        print('Python does not exist in skills')
else:
    print('Skills does not exist')

# 1C: If a person skills has only JavaScript and HTML, print('He is a front end developer'),
# if the person skills has Java, Python, SQL, print('He is a backend developer'), if the person skills
# has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
# for more accurate results more conditions can be nested!
print('1C: ')
front_end_count = 0
back_end_count = 0
for item in person['skills']:
    if item == 'Java' or item == 'Python' or item == 'SQL':
        back_end_count += 1
    elif item == 'JavaScript' or item == 'HTML':
        front_end_count += 1
print('front: ', front_end_count, ' back: ', back_end_count)
if front_end_count > 0 and back_end_count > 0:
    print('He is a fullstack developer')
elif front_end_count > 0 and back_end_count == 0:
    print('He is a front end developer')
elif front_end_count == 0 and back_end_count > 0:
    print('He is a backend developer')
else:
    print('Unknown title')

# 1D: If the person is married and if he lives in Ireland, print the information in the following format:
# Adam Strahan lives in Ireland. He is not married.
print('1D: ')
if person['is_married']:
    married = 'He is married.'
else:
    married = 'He is not married.'
print(person['first_name'], person['last_name'], 'lives in', person['country'], '.', married)

# Day 2: 30 Days of Python Programming

# Variables in Python
first_name = input('What is your first name?: ')
last_name = input('What is your last name?: ')
country = 'Ireland'
city = 'Carlow'
age = input('How old are you?: ')
is_married = False
skills = ['HTML', 'CSS', 'JS', 'Java', 'Python']
person_info = {
   'firstname':'Adam',
   'lastname':'Strahan',
   'country':'Ireland',
   'city':'Carlow'
   }

# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Adam'
print(first_name)               # 'Adam'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 'd', 'a', 'm']

# declaring multiple variables
month, day, date, year = "May", "Friday", 23, 1997
print(day, date, month, year)

# exercises
print("Length of first name: ", len(first_name))
print("Length of last name: ", len(last_name))
print("Total length : ", len(first_name) + len(last_name))
print("Difference in length : ", len(last_name) - len(first_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two
print("num_one = ", num_one)
print("num_two = ", num_two)
print("Total = ", total)
print("Difference = ", diff)
print("Product = ", product)
print("Division = ", division)
print("Remainder = ", remainder)
print("Num 1 to the power of Num 2 = ", exp)
print("Num 1 floor divison by Num 2 = ", floor_division)

# Circle maths
radius = float(input("What is the circle radius?: "))
pi = 3.14159
area = pi * (radius**2)
circumference = 2 * pi * radius
print("Area of circle with radius ", radius, " = ", area)
print("Circumference of circle with radius ", radius, " = ", circumference)
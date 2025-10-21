letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# ------Multi line Strings------
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# ------String Concatenation------
first_name = 'Adam'
last_name = 'Strahan'
space = ' '
full_name = first_name + space + last_name
print(full_name) # Adam Strahan
# Checking the length of a string using len() built-in function
print(len(first_name))  # 4
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 12

# ------Escape Sequences------
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# ------Old Style String Formatting------
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
# together with a format string, which contains normal text together with "argument specifiers",
# special symbols like "%s", "%d", "%f", "%.number of digitsf"
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
first_name = 'Adam'
last_name = 'Strahan'
language = 'Python'
formatted_string = 'I am %s %s. I am learning %s' %(first_name, last_name, language)
print(formatted_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
print(formatted_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formatted_string = 'The following are python libraries: %s' %python_libraries
print(formatted_string) # "The following are python libraries: ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

# ------New Style String Formatting------
first_name = 'Adam'
last_name = 'Strahan'
language = 'Python'
formatted_string = 'I am {} {}. I am learning {}'.format(first_name, last_name, language)
print(formatted_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formatted_string)

# ------String Interpolation / f-Strings------
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# ------String Interpolation / f-Strings------
language = 'Python'
a, b, c, d, e, f = language # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Accessing characters by index
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# String Slicing
language = 'Python'
first_three = language[0:3]  # starts at zero index and up to 3 but not include 3
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Reverse a string
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Skipping characters
language = 'Python'
pto = language[0:6:2]
print(pto) # Pto

# ------String Methods------
challenge = 'thirty days of python'

# capitalize(): Converts the first character of the string to capital letter
print('capitalize()')
print(challenge.capitalize())  # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..).
# The start is a starting indexing for counting and end is the last index to count.
print('count()')
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2`

# endswith(): Checks if a string ends with a specified ending
print('endswith()')
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
print('expandtabs()')
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
print('find()')
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.find('Adam')) # -1

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
print('rfind()')
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
print(challenge.rfind('Adam')) # -1

# format(): formats string into a nicer output
print('format()')
first_name = 'Adam'
last_name = 'Strahan'
age = 28
job = 'software developer'
country = 'Ireland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Adam Strahan. I am 28 years old. I am a software developer. I live in Ireland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

# index(): Returns the lowest index of a substring,
# additional arguments indicate starting and ending index (default 0 and string length - 1).
# If the substring is not found it raises a valueError.
print('index()')
sub_string = 'da'
print(challenge.index(sub_string))  # 7
# print(challenge.index(sub_string, 9))  error

# rindex(): Returns the highest index of a substring,
# additional arguments indicate starting and ending index (default 0 and string length - 1)
print('rindex()')
print(challenge.rindex(sub_string))  # 7
# print(challenge.rindex(sub_string, 9))  error
print(challenge.rindex('on', 8)) # 19

# isalnum(): Checks alphanumeric character
print('isalnum()')
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
print('isalpha()')
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)
print('isdecimal()')
challenge = 'thirty days of python'
print(challenge, ': ', challenge.isdecimal())  # False
challenge = '123'
print(challenge, ': ', challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge, ': ', challenge.isdecimal())   # False
challenge = '12 3'
print(challenge, ': ', challenge.isdecimal())  # False, space not allowed

# isdigit(): Checks if all characters in a string are numbers
# (0-9 and some other unicode characters for numbers)
print('isdigit()')
challenge = 'Thirty'
print(challenge, ': ', challenge.isdigit()) # False
challenge = '30'
print(challenge, ': ', challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge, ': ', challenge.isdigit())   # True

# isnumeric(): Checks if all characters in a string are numbers or number related
# (just like isdigit(), just accepts more symbols, like ½)
print('isnumeric()')
num = '10'
print(num, ': ', num.isnumeric()) # True
num = '\u00BD' # ½
print(num, ': ', num.isnumeric()) # True
num = '10.5'
print(num, ': ', num.isnumeric()) # False

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
print('isidentifier()')
challenge = '30DaysOfPython'
print(challenge, ': ', challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge, ': ', challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
print('islower()')
challenge = 'thirty days of python'
print(challenge, ': ', challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge, ': ', challenge.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase
print('isupper()')
challenge = 'thirty days of python'
print(challenge, ': ', challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge, ': ', challenge.isupper()) # True

# join(): Returns a concatenated string
print('join()')
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes all given characters starting from the beginning and end of the string
print('strip()')
challenge = 'thirty days of pythoonnn'
print(challenge, ': ', challenge.strip('noth')) # 'irty days of py'

# replace(): Replaces substring with a given string
print('replace()')
challenge = 'thirty days of python'
print(challenge, ': ', challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): Splits the string, using given string or space as a separator
print('split()')
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string
print('title()')
challenge = 'thirty days of python'
print(challenge, ': ', challenge.title()) # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase
print('swapcase()')
challenge = 'thirty days of python'
print(challenge, ': ', challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge, ': ', challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
print('startswith()')
challenge = 'thirty days of python'
print(challenge, ': ', challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge, ': ', challenge.startswith('thirty')) # False

# ------Exercises------
# 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
print('------Exercises------')
print('1: ')
thirty, days, of, python = 'Thirty ', 'Days ', 'Of ', 'Python'
concatenated_string = thirty + days + of + python
print(concatenated_string)

# 2: Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
print('2: ')
coding, for_string, all,  = 'Coding ', 'For ', 'All'
concatenated_string = coding + for_string + all
print(concatenated_string)

# 3: Declare a variable named company and assign it to an initial value "Coding For All"
print('3: ')
company = 'Coding For All'

# 4: Print the variable company using print()
print('4: ')
print(company)

# 5: Print the length of the company string using len() method and print().
print('5: ')
print(len(company))

# 6: Change all the characters to uppercase letters using upper() method.
print('6: ')
company = company.upper()
print(company)

# 7: Change all the characters to lowercase letters using lower() method.
print('7: ')
company = company.lower()
print(company)

# 8: Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print('8: ')
company = company.title()
print(company)

# 9: Cut(slice) out the first word of Coding For All string
print('9: ')
first = company.split()
print(first[0])

# 10: Check if Coding For All string contains a word Coding using the method index, find or other methods
print('10: ')
print(company.find('Coding'))
if(company.find('Coding') != -1) : print('String contains word.')
else : print('String does not contain word.')

# 11: Replace the word coding in the string 'Coding For All' to Python.
print('11: ')
print(company.replace('Coding', 'Python'))

# 12: Change Python for Everyone to Python for All using the replace method or other methods
print('12: ')
python_string = 'Python for Everyone'
print(python_string.replace('Everyone', 'All'))

# 13: Split the string 'Coding For All' using space as the separator (split())
print('13: ')
print(company.split(' '))

# 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print('14: ')
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))
print('Length of List: ', len(companies.split(', ')))

# 15: What is the character at index 0 in the string Coding For All
print('15: ')
print(company[0])

# 16: What is the last index of the string Coding For All
print('16: ')
print(company[len(company) - 1])

# 17: What character is at index 10 in "Coding For All" string
print('17: ')
print(company[10])

# 18: Create an acronym or an abbreviation for the name 'Python For Everyone'
print('18: ')
pfe_string = 'Python For Everyone'
words_split = pfe_string.split()
acronym = [word[0].upper() for word in words_split]
acr = ''.join(acronym)
print(acr)

# 19: Create an acronym or an abbreviation for the name 'Coding For All'
print('19: ')
abr = ''.join(word[0].upper() for word in company.split())
print(abr)

# 20: Use index to determine the position of the first occurrence of C in Coding For All
print('20: ')
print(company.index('C'))

# 21: Use index to determine the position of the first occurrence of F in Coding For All
print('21: ')
print(company.index('F'))

# 22: Use rfind to determine the position of the last occurrence of l in Coding For All People
print('22: ')
print(company.rfind('l'))

# 23: Use index or find to find the position of the first occurrence of the word 'because' in the following
# sentence: 'You cannot end a sentence with because because because is a conjunction'
print('23: ')
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
first_because = sentence.index('because')

# 24: Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('24: ')
print(sentence.rindex('because'))
end_because = sentence.rindex('because') + len('because')

# 25: Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print('25: ')
because = sentence[first_because : end_because]
print(because)

# 26: Find the position of the first occurrence of the word 'because' in the
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('26: ')
print(sentence.find('because'))

# 27: Slice out the phrase 'because because because' in the following sentence:
# # 'You cannot end a sentence with because because because is a conjunction'
print('27: ')
because = sentence[first_because : end_because]
print(because)

# 28: Does ''Coding For All' start with a substring Coding?
print('28: ')
print(company.startswith('Coding'))

# 29: Does 'Coding For All' end with a substring coding?
print('29: ')
print(company.endswith('coding'))

# 30: '   Coding For All      '  , remove the left and right trailing spaces in the given string
print('30: ')
spaced_string = '   Coding For All      '
print(spaced_string.strip())

# 31: Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython or thirty_days_of_python
print('31: ')
identifier = '30DaysOfPython'
print(identifier.isidentifier())
identifier = 'thirty_days_of_python'
print(identifier.isidentifier())

# 32: The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
print('32: ')
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# 33: Use the new line escape sequence to separate the following sentences:
# I am enjoying this challenge. I just wonder what is next.
print('33: ')
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34: Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Adam      28      Ireland   Carlow
print('34: ')
print('Name\tAge\tCompany\tCity')
print('Adam\t28\tIreland\tCarlow')

# 35: Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print('35: ')
radius, pi = 10, 3.14
area = pi * radius ** 2
formatted = 'The area of a circle with radius {} is {}'.format(radius, area)
print(formatted)

# 36: Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
print('36: ')
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

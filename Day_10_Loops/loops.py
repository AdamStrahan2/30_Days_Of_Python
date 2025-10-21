from Data.countries import countries
from Data.countries_data import countries_info
from collections import Counter

# ------ Loops ------
#  In order to handle repetitive task programming languages use loops.
#  Python programming language also provides the following types of two loops:
#  1) While Loop  2) For Loop

# ------ While Loops ------

# Used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false, the lines of code after the loop will be continued to be executed.
count = 0
while count < 5:
    print(count)
    count = count + 1

# If we want to run a block of code once the condition is no longer true, we can use else.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print('Final Count from else block: ', count)

# ------ Break and Continue 1 ------

# We use break when we want to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# With the continue statement we can skip the current iteration, and continue with the next.
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue    # Skips 3 without printing
    print(count)
    count = count + 1

# ------ For Loops ------

# Loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number is temporary name to refer to the list's items, valid only inside this loop
    print('For Loop: ', number)       # the numbers will be printed line by line, from 0 to 5

# String For Loop
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# Tuple For Loop
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# Dictionary For Loop. Gets Keys
person = {
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
for key in person:
    print(key)

for key, value in person.items():
    print(key, ':', value)  # this way we get both keys and values printed out

# Set For Loops
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# ------ Break and Continue 2 ------

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

# if the number equals 3, the step after the condition (but inside the loop) is skipped and the
# execution of the loop continues if there are any iterations left.
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")  # for short hand conditions need both if and else statements
print('outside the loop')

# ------ Range Function ------

# The range() function is used list of numbers. The range(start, end, step) takes three parameters:
# starting, ending and increment. By default it starts from 0 and the increment is 1.
# The range sequence needs at least 1 argument (end).
lst = list(range(11))
print('list: ', lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print('set: ', st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print('list: ', lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print('set: ', st)  # {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# ------ Nested For Loops ------

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# ------ For Else ------

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# ------ Pass ------

# when statement is required (after semicolon), but we don't like to execute any code there,
# we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for number in range(6):
    pass

# ------ Exercises 1 ------
# 1: Iterate 0 to 10 using for loop, do the same using while loop.
print('1: ')
for number in range(11):
    print('for loop: ', number)

count = 0
while count < 11:
    print('while loop: ', count)
    count += 1

# 2: Iterate 10 to 0 using for loop, do the same using while loop.
print('2: ')
for number in range(10, -1, -1):
    print('for loop: ', number)

count = 10
while count >= 0:
    print('while loop: ', count)
    count -= 1

# 3: Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
print('3: ')
# Outer loop for rows
for i in range(7):
    # Inner loop to print hashes for each row
    # (i + 1) ensures that the number of hashes increases with each row
    for j in range(i + 1):
        print("#", end="")  # end="" prevents print() from adding a newline character at the end
    # Print a newline character to start a new row after the inner loop finishes
    print()

# 4: Use nested loops to create the following:
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
#   # # # # # # # #
print('4: ')
for i in range(8):
    for j in range(8):
        print('#', end='')
    print()

# 5: Print the following pattern:
#   0 x 0 = 0
#   1 x 1 = 1
#   2 x 2 = 4
#   3 x 3 = 9
#   4 x 4 = 16
#   5 x 5 = 25
#   6 x 6 = 36
#   7 x 7 = 49
#   8 x 8 = 64
#   9 x 9 = 81
#   10 x 10 = 100
print('5: ')
for i in range(11):
    print(i, 'x', i, '=', (i * i))

# 6: Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop
# and print out the items.
print('6: ')
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

# 7: Use for loop to iterate from 0 to 100 and print only even numbers
print('7: ')
for num in range(0, 101, 2):
    print('even: ', num)

# 8: Use for loop to iterate from 0 to 100 and print only odd numbers.
print('8: ')
for num in range(1, 100, 2):
    print('odd: ', num)

# ------ Exercises 2 ------

# 1: Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print('1: ')
total = 0
for i in range(0, 101):
    print('num: ', i)
    print('total: ', total)
    total += i
    print('new total: ', total)
print('Sum of all numbers 0-100 = ', total)


# 2: Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print('2: ')
even_total = 0
odd_total = 0
for even in range(0, 101, 2):
    print('num: ', even)
    print('even_total: ', even_total)
    even_total += even
    print('new even_total: ', even_total)
print('Sum of all evens: ', even_total)

for odd in range(1, 100, 2):
    print('num: ', even)
    print('odd_total: ', odd_total)
    odd_total += odd
    print('new odd_total: ', odd_total)
print('Sum of all odds: ', odd_total)

# ------ Exercises 3 ------

# 1: Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries containing the word land.
print('1: ')
countries_with_land = 0
for i in countries:
    if i.find('land') != -1:
        print(i)
        countries_with_land += 1
    else:
        continue
print('Total countries with "land" in the name: ', countries_with_land)

# 2: This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print('2: ')
fruit = ['banana', 'orange', 'mango', 'lemon']
print('fruit: ', fruit)
reversed_fruit = []
for i in range(len(fruit)-1, -1, -1):
    print(fruit[i])
    reversed_fruit.append(fruit[i])
print('reversed_fruit: ', reversed_fruit)

# 3: Go to the data folder and use the countries_data.py file.
# A: What are the total number of languages in the data

print('3A: ')
languages = set()
for country in countries_info:
    languages.update(country['languages'])
print(languages)
print("Total number of languages: ", len(languages))

# B: Find the ten most spoken languages from the data
print('3B: ')
# Flatten the list of all languages from all countries
all_languages = [lang for country in countries_info for lang in country["languages"]]
print('all_languages: ', all_languages)
print('Length of all_languages: ', len(all_languages))
# Count the occurrences of each language
language_counts = Counter(all_languages)
# Get the top 10 most common languages
top_10_languages = language_counts.most_common(10)
print("Top 10 most common languages:")
for language, count in top_10_languages:
    print(f"{language}: {count}")

# C: Find the 10 most populated countries in the world
print('3C: ')
# Sort countries by population in descending order
sorted_countries = sorted(countries_info, key=lambda c: c["population"], reverse=True)
print(sorted_countries)
# Get the top 10 most populated countries
top_10_populated = sorted_countries[:10]
# Print results
print("Top 10 most populated countries:")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']: ,}")
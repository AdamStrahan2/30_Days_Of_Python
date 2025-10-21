# There are four collection data types in Python :
#
# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

# ------ Creating Lists ------

# Built in List Functions
lst = list()
print(lst)

empty_list = list() # this is an empty list, no item in the list
print('List Size: ', len(empty_list)) # 0

# Square Brackets
lst = []
empty_list = [] # this is an empty list, no item in the list
print('List Size: ', len(empty_list)) # 0

# Lists with Values
fruits = ['banana', 'orange', 'mango', 'lemon']                      # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']       # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']              # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']    # list of countries

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# list containing different data types
lst = ['Adam', 28, True, {'country': 'Ireland', 'city': 'Carlow'}]
print(lst)

# ------ Indexing ------

# Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

# ------ Unpacking List ------
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst # Use * to assign the rrst of the list
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# First Example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']

# Second Example about unpacking list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

# Third Example about unpacking list
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, ic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(ic)
print(es)

# ------ Slicing From List ------

# Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
print(all_fruits)
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(all_fruits)
orange_and_mango = fruits[1:3] # it does not include the first index
print(orange_and_mango)
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']
print(orange_and_lemon)

# Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
print(all_fruits)
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
print(orange_and_mango)
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
print(orange_mango_lemon)
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
print(reverse_fruits)

# ------ Modifying Lists ------

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# ------ Checking Items In List ------

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# ------ Adding Items To List ------

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

# ------ Inserting Items Into List ------

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango (Index 2)
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

# ------ Removing Items From List ------

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

# pop() removes from specified index
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# del keyword
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
# print(fruits)       This should give: NameError: name 'fruits' is not defined

# ------ Clear List ------

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# ------ Copying List ------

fruits = ['banana', 'orange', 'mango', 'lemon']
print('fruits: ', fruits)
new_fruits = []

# This will duplicate the list, changes to one affects the other
new_fruits = fruits
print('new_fruits: ', new_fruits) # ['banana', 'orange', 'mango', 'lemon']
new_fruits.append('lime')
print('append lime to new_fruits')
print('fruits: ', fruits)   # ['banana', 'orange', 'mango', 'lemon', 'lime']
print('new_fruits: ', new_fruits)   # ['banana', 'orange', 'mango', 'lemon', 'lime']
fruits.remove('lime')
print('remove lime from fruits')
print('fruits: ', fruits)   # ['banana', 'orange', 'mango', 'lemon']
print('new_fruits: ', new_fruits)   # ['banana', 'orange', 'mango', 'lemon']

# This will copy the list, changes to one won't affect the other
fruits_copy = fruits.copy()
print('fruits: ', fruits)   # ['banana', 'orange', 'mango', 'lemon']
print('fruits_copy: ', fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print('append apple to fruits')
print('fruits: ', fruits)   # ['banana', 'orange', 'mango', 'lemon', 'apple']
print('fruits_copy: ', fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
fruits_copy.append('kiwi')
print('append kiwi to fruits_copy')
print('fruits: ', fruits)   # ['banana', 'orange', 'mango', 'lemon', 'apple']
print('fruits_copy: ', fruits_copy)       # ['banana', 'orange', 'mango', 'lemon', 'kiwi']
print('new_fruits: ', new_fruits)   # ['banana', 'orange', 'mango', 'lemon', 'apple']

# ------ Joining Lists ------

# Use + Operator
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# Use extend()
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# ------ Counting Items in List ------

# Use count() to return number of times item appears in list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# ------ Finding Index of Item in List ------

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, shows the first occurrence

# ------ Reversing a List ------

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]

# ------ Sorting a List ------

# sort() modifies original list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

# sorted() returns the ordered list without modifying original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']

# ------ Exercises ------
# 1: Declare an empty list
print('1: ')
new_games = []
print('new_games: ', new_games)

# 2: Declare a list with more than 5 items
print('2: ')
old_games = ['Spyro', 'Crash', 'GTA', 'Burnout', 'Saints Row', 'Mario', 'Sonic']
print('old_games: ', old_games)

# 3: Find the length of your list
print('3: ')
print('Length of old_games: ', len(old_games))

# 4: Get the first item, the middle item and the last item of the list
length = len(old_games)
print('Length: ', length)
if length <= 0:
    print('List is empty')
else:
    first_game = old_games[0]
    last_game = old_games[length - 1]
    if length % 2 == 1:
        middle_game = old_games[length // 2]
    elif length % 2 == 0:
        even_index_low = length // 2 -1
        even_index_high = length // 2 + 1
        print('even_index_low: ', even_index_low, ' : even_index_high: ', even_index_high)
        middle_game = old_games[even_index_low : even_index_high]
    print('First Game: ', first_game)
    print('Middle Game: ', middle_game)
    print('Last Game: ', last_game)

# 5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print('5: ')
mixed_data_types = ['Adam', 28, 1.7, 'In a relationship', 'Carlow']
print(mixed_data_types)

# 6: Declare a list variable named it_companies and assign initial values:
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print('6: ')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7: Print the list using print()
print('7: ')
print(it_companies)

# 8: Print the number of companies in the list
print('8: ')
length = len(it_companies)
print('Length: ', length)


# 9: Print the first, middle and last company
print('9: ')
first_company = it_companies[0]
last_company = it_companies[length - 1]
middle_company = it_companies[length // 2]
print('First Company: ', first_company)
print('Middle Company: ', middle_company)
print('Last Company: ', last_company)

# 10: Print the list after modifying one of the companies
print('10: ')
it_companies[4] = 'ibm'
print(it_companies)

# 11: Add an IT company to it_companies
print('11: ')
it_companies.append('Oscorp')
print(it_companies)

# 12: Insert an IT company in the middle of the companies list
print('12: ')
new_company = 'Aperture Science'
it_companies = it_companies[:len(it_companies) // 2] + [new_company] + it_companies[len(it_companies) // 2:]
print(it_companies)

# 13: Change one of the it_companies names to uppercase
print('13: ')
it_companies[5] = it_companies[5].swapcase()
print(it_companies)

# 14: Join the it_companies with a string '#;  '
print('14: ')
print('#; '.join(it_companies))
print(it_companies)

# 15: Check if a certain company exists in the it_companies list
print('15: ')
does_exist = 'Google' in it_companies
print('Google in list?: ', does_exist)
does_exist = 'Black Mesa' in it_companies
print('Black Mesa in list?: ', does_exist)

# 16: Sort the list using sort() method
print('16: ')
it_companies.sort()
print(it_companies)

# 17: Reverse the list in descending order using reverse() method
print('17: ')
it_companies.reverse()
print(it_companies)

# 18: Slice out the first 3 companies from the list
print('18: ')
first_three = it_companies[:3]
print(first_three)

# 19: Slice out the last 3 companies from the list
print('19: ')
last_three = it_companies[-3:]
print(last_three)

# 20: Slice out the middle IT company or companies from the list
print('20: ')
length = len(it_companies)
if length % 2 == 1:
    middle = it_companies[length // 2]
elif length % 2 == 0:
    even_index_low = length // 2 - 1
    even_index_high = length // 2 + 1
    middle = it_companies[even_index_low : even_index_high]
print('Middle Company: ', middle)

# 21: Remove the first IT company from the list
print('21: ')
it_companies.pop(0)
print(it_companies)

# 22: Remove the middle IT company or companies from the list
print('22: ')
length = len(it_companies)
if length % 2 == 1:
    middle = it_companies[length // 2]
    it_companies.pop(middle)
elif length % 2 == 0:
    even_index_low = length // 2 - 1
    even_index_high = length // 2 + 1
    del it_companies[even_index_low : even_index_high]
print(it_companies)

# 23: Remove the last IT company from the list
print('23: ')
it_companies.pop()
print(it_companies)

# 24: Remove all IT companies from the list
print('24: ')
it_companies.clear()
print(it_companies)

# 25: Destroy the IT companies list
print('25: ')
del it_companies

# 26: Join the following lists: front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
print('26: ')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)

# 27: After joining the lists in Q26 copy the joined list and assign it to a variable full_stack,
# then insert Python and SQL after Redux.
print('27: ')
full_stack = new_list.copy()
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print('full_stack: ', full_stack)
print('new_list: ', new_list)

# ------ Exercises 2 ------

# 1: The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# A: Sort the list and find the min and max age
print('1A:')
ages.sort()
min = ages[0]
max = ages[len(ages) - 1]
print('ages sorted: ', ages)
print('youngest: ', min)
print('oldest: ', max)

# 1B: Add the min age and the max age again to the list
print('1B:')
ages.append(min)
ages.append(max)
print('Max and Min added: ', ages)
ages.sort()
print('Sorted: ', ages)

# 1C: Find the median age (one middle item or two middle items divided by two)
print('1C: ')
length = len(ages)
if length % 2 == 1:
    median = length // 2
    print('Median Age: ', ages[median])
elif length % 2 == 0:
    even_index_low = length // 2 - 1
    even_index_high = length // 2
    median = (ages[even_index_low] + ages[even_index_high]) / 2
    print('Median Age: ', median)

# 1D: Find the average age (sum of all items divided by their number )
print('1D: ')
total = 0
for age in ages:
    total += age
avg = total / len(ages)
print('Average: ', avg)

# 1E: Find the range of the ages (max minus min)
print('1D: ')
min = ages[0]
max = ages[len(ages) - 1]
range = max - min
print('Range: ', range)

# 1F: Compare the value of (min - average) and (max - average), use abs() method
print('1F: ')
value_min = abs(min - avg)
value_max = abs(max - avg)
print('Min - Avg = ', value_min)
print('Max - Avg = ', value_max)
print('Difference: ', abs(value_min - value_max))

# 1: Find the middle country(ies) in the countries list
print('1: ')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
length = len(countries)
print('Countries: ', length)
middle_index = length // 2
print('Middle Country: ', countries[middle_index])

# 2: Divide the countries list into two equal lists if it is even if not one more country for the first half
print('2: ')
first_half = countries[:middle_index + 1]
second_half = countries[middle_index + 1:]
print('Length of First List: ', len(first_half), ' and Second List: ', len(second_half))
print('First: ', first_half)
print('Second: ', second_half)

# 3: ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries
# and the rest as scandic countries.
print('3: ')
short_country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = short_country_list
print('Ch: ', ch, ' Ru: ', ru, ' Us: ', us, 'Scandic Countries: ', scandic)







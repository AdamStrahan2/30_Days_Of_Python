# ------ Regular Expressions ------

# A regular expression or RegEx is a special text string that helps to find patterns in data.
# A RegEx can be used to check if some pattern exists in a different data type.
# To use RegEx in python first we should import the RegEx module which is called re.
import keyword
import re
from collections import Counter

# ------ Methods in re Module ------

# To find a pattern we use different set of re character sets that allows to search for a match in a string.
#   - re.match(): searches only in the beginning of the first line of the string and returns matched objects
#                 if found, else returns None.
#   - re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
#   - re.findall: Returns a list containing all matches
#   - re.split: Takes a string, splits it at the match points, returns a list
#   - re.sub: Replaces one or many matches within a string

# ------ Match ------

txt = 'I love to learn python and javaScript'
# It returns an object with span and match
match = re.match('I love to learn', txt, re.I)
# 'I love to learn' is a string or a pattern, txt is the text we look for a pattern , re.I is case ignore
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach

# The match function returns an object only if the text starts with the pattern.
match = re.match('I like to teach', txt, re.I)
print(match)  # None

# ------ Search ------

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

# Search is better than Match as it can look for the pattern throughout the text.
# Search returns a match object with a first match that was found, otherwise it returns None.

# ------ Findall ------

# This function checks for the pattern through the whole string and returns all the matches as a list.
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

# As re.I is used, the search is not case sensitive
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']
matches = re.findall('python', txt)
print(matches)  # ['python']

# Alternative ways to handle case sensitivity
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

# ------ Replacing a Substring ------

match_replaced = re.sub('Python|python', 'JavaScript', txt, flags=re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, flags=re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

txt = '''%I a%m a te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fi%nd te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

# ------ Splitting Text Using RegEx Split ------

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))  # splitting using \n - end of line symbol

# ------ Writing RegEx Patterns ------

# To declare a string variable we use a single or double quote. To declare RegEx variable r''.
# The following pattern only identifies apple with lowercase, to make it case insensitive either
# we should rewrite our pattern or add a flag.

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day keeps the doctor away has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# ------ Character Sets ------

# []          - A set of characters
# [a-c]       - a or b or c
# [a-z]       - any letter from a to z
# [A-Z]       - any character from A to Z
# [0-3]       - 0 or 1 or 2 or 3
# [0-9]       - any number from 0 to 9
# [A-Za-z0-9] - any single character, that is a to z, A to Z or 0 to 9

# ------ Escape Characters ------

# \           - uses to escape special characters
#   \d        - match where the string contains digits (numbers from 0-9)
#   \D        - match where the string does not contain digits
#   .         - any character except new line character(\n)

# ------ Character Patterns ------

# ^                 - starts with
#   r'^substring'   - a sentence that starts with a word substring
#   r'[^abc]        - not a, not b, not c.

# $                 - ends with
#   r'substring$'   - sentence that ends with a word substring

# *                 - zero or more times
#   r'[a]*'         - optional or it can occur many times.

# +                 - one or more times
#   r'[a]+'         - at least once (or more)

# ?                 - zero or one time
#   r'[a]?'         - zero times or once

# {3}               - Exactly 3 characters
# {3,}              - At least 3 characters
# {3,8}             - 3 to 8 characters

# |                 - Either or
#   r'apple|banana' - means either apple or a banana

# ()                - Capture and group

# ------ Examples ------

txt = 'Apple and banana are fruits. An old cliche says an apple a day keeps the doctor away has been replaced by a banana a day keeps the doctor far far away.'

# Square Bracket
regex_pattern = r'[Aa]pple'  # this square bracket mean either A or a
matches = re.findall(regex_pattern, txt)
print('Square Bracket:', matches)  # ['Apple', 'apple']

regex_pattern = r'[Aa]pple|[Bb]anana'  # this square bracket means either [A or a] or [B or b]
matches = re.findall(regex_pattern, txt)
print('Square Bracket:', matches)  # ['Apple', 'banana', 'apple', 'banana']

# Escape Character
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on November 4, 2025 and revised on November 6, 2025.'
matches = re.findall(regex_pattern, txt)
print('Escape Character (d):', matches)  # ['4', '2', '0', '2', '5', '6', '2', '0', '2', '5'], not what we want

# One or More Times (+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
matches = re.findall(regex_pattern, txt)
print('Escape Character (d+):', matches)  # ['4', '2025', '6', '2025'], this is better!

# Period (.)
regex_pattern = r'[a].'  # square bracket means 'a' and . means any character after 'a' except new line
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print('Period ([a].):', matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print('Period ([a].+):', matches)  # ['and banana are fruits']

# Zero or More Times (*)
regex_pattern = r'[n].*'  # . any character, * any character zero or more times
matches = re.findall(regex_pattern, txt)
print('Zero or More Times ([n].*):', matches)  # ['nd banana are fruits']

# Zero or One Time (?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? here means that '-' is optional
matches = re.findall(regex_pattern, txt)
print('Zero or One Time ([Ee]-?mail):', matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifier ({})
txt = 'This regular expression example was made on November 4, 2025 and revised on November 6, 2025.'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print('Quantifier (\\d{4}):', matches)  # ['2025', '2025']

txt = 'This regular expression example was made on November 4, 2025 and revised on November 6, 2025.'
regex_pattern = r'\d{1,4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print('Quantifier (\\d{1,4}):', matches)  # ['4', '2025', '6', '2025']

# Cart (^)
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print('Cart (^This):', matches)  # ['This']

regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print('Cart ([^A-Za-z ]+):', matches)  # ['4,', '2025', '6,', '2025.']

# ------ Exercises 1 ------

# 1: What is the most frequent word in the following paragraph?
paragraph = '''I love teaching. If you do not love teaching what else can you love.
            I love Python if you do not love something which can give you all the
            capabilities to develop an application what else can you love.'''
print('1:')
print(paragraph)
# change to lower case
text = paragraph.lower()

# use regex to remove punctuation
words = re.findall(r'\b\w+\b', text)  # extracts each word from text

word_counts = Counter(words)
print('word_counts:', word_counts)
most_common_word = word_counts.most_common(1)
print('Most Common Word:', most_common_word)  # Most Common Word: [('love', 6)]

# 2: Extract these numbers from this whole text and find the distance between the two furthest particles.
print('2:')
text = '''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction,
0 at origin, 4 and 8 in the positive direction.'''
numbers = re.findall(r'-?\d+', text)  # Filter out all digits along with optional negative
print('numbers:', numbers)
numbers = [int(n) for n in numbers]  # Convert strings to integers
numbers.sort()
print('numbers:', numbers)
distance = max(numbers) - min(numbers)
print('Distance:', distance)

# ------ Exercises 2 ------

# 1: Write a pattern which identifies if a string is a valid python variable
# A valid Python variable name:
# Must start with a letter (a–z or A–Z) or an underscore (_)
# Can be followed by letters, digits (0–9), or underscores
# Cannot start with a digit
# Cannot be a Python keyword (like for, class, if, etc.)
print('1:')
def is_valid_variable(var):
    # ^         - Start of the string
    # [a-zA-Z_] - First character must be a letter or underscore
    # \w*       - Followed by zero or more word characters (a-zA-Z0-9_)
    # $         - End of the string
    pattern = r'^[a-zA-Z_]\w*$'
    return re.match(pattern, var) and not keyword.iskeyword(var)

tests = ['first_name', '1st_name', 'first-name', '_first_name', 'class', 'valid_var123']
for t in tests:
    print(f"{t:12} → {is_valid_variable(t)}")


# ------ Exercises 3 ------

# 1: Clean the following text. After cleaning, count three most frequent words in the string.
print('1:')
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(para):
    cleaned = re.sub(r'[^a-zA-Z\s]', '', para)  # Remove all non letter or space characters
    cleaned = re.sub(r'\s+', ' ', cleaned)      # Replace multi space with single space
    return cleaned.strip()

def most_frequent_words(para):
    words = para.split()
    word_counts = Counter(words)
    return [(count, word) for word, count in word_counts.most_common(3)]

cleaned_text = clean_text(sentence)
print('cleaned_text:', cleaned_text)
print('Most Common Words:', most_frequent_words(cleaned_text))



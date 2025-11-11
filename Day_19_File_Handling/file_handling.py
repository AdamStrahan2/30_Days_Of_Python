# ------ File Handling ------

import os
import json
import csv
#import xlrd
import xml.etree.ElementTree as ET
from collections import Counter
import re
import math

# So far we have seen different Python data types. We usually store our data in different file formats.
# In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel)
# in this section. First, let us get familiar with handling files with common file format(.txt).
# File handling is an import part of programming which allows us to create, read, update and delete files.
# In Python to handle data we use open() built-in function.

# Syntax
# open('filename', mode)  # mode(r, a, w, x, t,b)  could be to read, write, update

# "r" - Read   - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write  - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text   - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# ------ Opening Files for Reading ------

# Check current working directory
print(os.getcwd())

# The default mode of open is reading, so we do not have to specify 'r' or 'rt'.
# I have created and saved a file named reading_file_example.txt in the files directory.
f = open('../files/reading_file_example.txt')  # '../' is to move back up one directory
print(f)  # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='cp1252'>
f.close()

# I printed the opened file and it gave some information about it.
# Opened file has different reading methods: read(), readline, readlines.
# An opened file has to be closed with close() method.

# read(): read the whole text as string. If we want to limit the number of characters we want to read,
# we can limit it by passing int value to the read(number) method.
f = open('../files/reading_file_example.txt')
txt = f.read()
print('File Type:', type(txt))
print('txt:', txt)
f.close()

f = open('../files/reading_file_example.txt')
txt = f.read(10)
print('txt.read(10):', txt)
f.close()

# readline(): read only the first line
f = open('../files/reading_file_example.txt')
line = f.readline()
print('Type:', type(line))
print('readline():', line)
f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open('../files/reading_file_example.txt')
lines = f.readlines()
print('Type:', type(lines))  # Type: <class 'list'>
print('readlines():', lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('../files/reading_file_example.txt')
lines = f.read().splitlines()
print('Type:', type(lines))  # Type: <class 'list'>
print('splitlines():', lines)
f.close()

# After we open a file, we should close it. It's easy to forget to close them.
# Opening files using 'with' closes the files by itself.
# Let us rewrite the the previous example with the with method:
with open('../files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print('with - Type:', type(lines))
    print('with - splitlines():', lines)

# ------ Opening Files for Writing and Updating ------

# To write to an existing file, we must add a mode as parameter to the open() function:
# "a" - append - will append to the end of the file, if the file does not it creates a new file.
# "w" - write  - will overwrite any existing content, if the file does not exist it creates.
# Let us append some text to the file we have been reading:
with open('../files/reading_file_example.txt', 'a') as f:
    f.write('\nThis text has to be appended at the end.')
    print(f)

# The method below creates a new file, if the file does not exist:
with open('../files/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file.')
    print(f)

# ------ Deleting Files ------

# Create example file to be deleted
#with open('../files/example.txt', 'a') as f:
#    f.write('Example text for deletion')

# To remove a file we use os module.
# If the file does not exist, the remove method will raise an error, so we use a condition like this:
if os.path.exists('../files/example.txt'):
    os.remove('../files/example.txt')
    print('File Deleted!')
else:
    print('File does not exist!')

# ------ File Types ------

# --- Files with txt Extension ---
# File with txt extension is a very common form of data and we have covered it in the previous section.

# --- Files with JSON Extension ---
# JSON stands for JavaScript Object Notation. It is a stringified JavaScript object or Python dictionary.
# dictionary
person_dct = {
    "name": "Adam",
    "country": "Ireland",
    "city": "Carlow",
    "skills": ["JavaScript", "Java", "Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Adam', 'country': 'Ireland', 'city': 'Carlow', 'skills': ['JavaScript', 'Java', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name": "Adam",
    "country": "Ireland",
    "city": "Carlow",
    "skills": ["JavaScript", "Java", "Python"]
}'''

# ------ Changing JSON to Dictionary ------

# To change a JSON to a dictionary, first we import the json module and then we use loads method.
# JSON
person_json = '''{
    "name": "Adam",
    "country": "Ireland",
    "city": "Carlow",
    "skills": ["JavaScript", "Java", "Python"]
}'''

# change JSON to dictionary
person_dct = json.loads(person_json)
print('Type:', type(person_dct))
print('person_dct:', person_dct)
print('person_dct[name]:', person_dct['name'])

# ------ Changing Dictionary to JSON ------

# To change a dictionary to a JSON we use dumps method from the json module.
# python dictionary
person = {
    "name": "Adam",
    "country": "Ireland",
    "city": "Carlow",
    "skills": ["JavaScript", "Java", "Python"]
}
# Convert it to JSON
person_json = json.dumps(person, indent=4)  # indent could be 2, 4, 8. It beautifies the json
print('Type:', type(person_json))  # JSON is a string type
print('person_json:', person_json)

# ------ Saving As A JSON File ------

# We can also save our data as a json file. For writing a json file, we use the json.dump() method,
# it can take dictionary, output file, ensure_ascii and indent.
# python dictionary
person = {
    "name": "Adam",
    "country": "Ireland",
    "city": "Carlow",
    "skills": ["JavaScript", "Java", "Python"]
}

with open('../files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
# In the code above, we use encoding and indentation. Indentation makes the json file easy to read.

# ------ CSV Files ------

# CSV stands for comma separated values.
# CSV is a simple file format used to store tabular data, such as a spreadsheet or database.
# CSV is a very common data format in data science.
with open('../files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')  # reader method to read csv file
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a software developer. He lives in {row[2]}, {row[1]}.')
            line_count += 1
    print(f'Number of lines: {line_count}')

# ------ XLSX Files ------

# To read excel files we need to install xlrd package.
# We will cover this after we cover package installing using pip.
#excel_book = xlrd.open_workbook('sample.xls')
#print(excel_book.nsheets)
#print(excel_book.sheet_names)

# ------ XML Files ------

# XML is another structured data format which looks like HTML. In XML the tags are not predefined.
# First line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute.
tree = ET.parse('../files/xml_example.xml')
root = tree.getroot()
print('Root Tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('Field:', child.tag)

# ------ Exercises 1 ------

# 1: Write a function which counts the number of lines and words in a text. All files are in the data folder:
print ('1:')
def count_lines_and_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        num_lines = len(lines)
        # Split all lines into words
        words = [word for line in lines for word in line.split()]
        num_words = len(words)
    return num_lines, num_words

# Build path relative to the script
base_path = os.path.dirname(__file__)

# A: Read barrack_obama_speech.txt file and count number of lines and words
print('A: Barrack Obama')
file_path = os.path.join(base_path, '..', 'data', 'barrack_obama_speech.txt')
lines, words = count_lines_and_words(file_path)
print(f'Lines: {lines}   Words: {words}')

# B: Read michelle_obama_speech.txt file and count number of lines and words
print('B: Michelle Obama')
file_path = os.path.join(base_path, '..', 'data', 'michelle_obama_speech.txt')
lines, words = count_lines_and_words(file_path)
print(f'Lines: {lines}   Words: {words}')

# C: Read donald_trump_speech.txt file and count number of lines and words
print('C: Donald Trump')
file_path = os.path.join(base_path, '..', 'data', 'donald_trump_speech.txt')
lines, words = count_lines_and_words(file_path)
print(f'Lines: {lines}   Words: {words}')

# D: Read melania_trump_speech.txt file and count number of lines and words
print('D: Melania Trump')
file_path = os.path.join(base_path, '..', 'data', 'melania_trump_speech.txt')
lines, words = count_lines_and_words(file_path)
print(f'Lines: {lines}   Words: {words}')

# 2: Read the countries_data.json data file in data directory,
# create a function that finds the ten most spoken languages
print('2:')
def most_spoken_languages(file_path, top_n=10):
    # Read JSON file
    with open(file_path, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    # Collect all languages
    all_languages = []
    for country in countries:
        all_languages.extend(country.get('languages', []))

    # Count how often each language appears
    language_counts = Counter(all_languages)
    return language_counts.most_common(top_n)

# Build the correct file path
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', 'data', 'countries_data.json')

# Call the function
top_languages = most_spoken_languages(file_path)
print("Top 10 most spoken languages:")
for lang, count in top_languages:
    print(f"{lang}: {count}")

top_languages = most_spoken_languages(file_path, 3)
print("Top 3 most spoken languages:")
for lang, count in top_languages:
    print(f"{lang}: {count}")

# 3: Read the countries_data.json data file in data directory, create a function that
# creates a list of the ten most populated countries
print('3:')
def most_populated_countries(file_path, top_n=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        countries = json.load(f)

    sorted_countries = sorted(countries, key=lambda x: x.get('population', 0), reverse=True)
    top_countries = sorted_countries[:top_n]
    result = [{'country': c['name'], 'population': c['population']} for c in top_countries]
    return result

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', 'data', 'countries_data.json')

top_3_populated = most_populated_countries(file_path, 3)
top_10_populated = most_populated_countries(file_path)

print("Top 10 Most Populated Countries:")
for country in top_10_populated:
    print(f"{country['country']}: {country['population']:,}")

print("Top 3 Most Populated Countries:")
for country in top_3_populated:
    print(f"{country['country']}: {country['population']:,}")

# ------ Exercises 2 ------

# 4: Extract all incoming email addresses as a list from the email_exchange_big.txt file.
print('4:')
def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # RegEx to match email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # Find all matches
    emails = re.findall(email_pattern, text)
    # Remove duplicates
    unique_emails = list(set(emails))
    return unique_emails

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', 'data', 'email_exchange_big.txt')

emails = extract_emails(file_path)
print(f"Total emails found: {len(emails)}")
print("Sample emails:", emails[:10])  # Show first 10

# 5: Find the most common words in the English language. Call the name of your function
# find_most_common_words, it will take two parameters - a string or a file and a positive integer,
# indicating the number of words. Your function will return an array of tuples in descending order.
print('5:')
def find_most_common_words(source, n=10):
    # Check if file path or text
    if os.path.exists(source):
        with open(source, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = source

    # Clean text: remove punctuation and make lowercase
    text = re.sub(r'[^A-Za-z\s]', '', text).lower()

    # Split into words
    words = text.split()

    # Count words
    word_counts = Counter(words)
    return word_counts.most_common(n)

# Example 1 — using a text string
text = """
I love Python programming. Python is fun, powerful, and easy to learn.
The more I use Python, the more I love it.
"""
print('Text Example:', find_most_common_words(text, 5))

# Example 2 — using a file
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', 'data', 'barrack_obama_speech.txt')
print('File Example:', find_most_common_words(file_path, 10))

# 6: Use the function, find_most_common_words to find:
# A: The ten most frequent words used in Obama's speech
# B: The ten most frequent words used in Michelle's speech
# C: The ten most frequent words used in Trump's speech
# D: The ten most frequent words used in Melania's speech
print('6:')
print('A: Obama')
file_path = os.path.join(base_path, '..', 'data', 'barrack_obama_speech.txt')
print(find_most_common_words(file_path))
print('B: Michelle')
file_path = os.path.join(base_path, '..', 'data', 'michelle_obama_speech.txt')
print(find_most_common_words(file_path))
print('C: Trump')
file_path = os.path.join(base_path, '..', 'data', 'donald_trump_speech.txt')
print(find_most_common_words(file_path))
print('D: Melania')
file_path = os.path.join(base_path, '..', 'data', 'melania_trump_speech.txt')
print(find_most_common_words(file_path))

# 7: Write a python application that checks similarity between two texts.
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
# For instance check the similarity between the transcripts of Michelle's and Melania's speech.
# You may need a couple of functions, function to clean the text(clean_text),
# function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
# List of stop words are in the data directory
print('7:')
def clean_text(text):
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove punctuation
    text = text.lower()                      # Convert to lowercase
    return text

def remove_support_words(text, stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as f:
        stop_words = set(f.read().split())

    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return ' '.join(filtered)

def check_text_similarity(text1, text2):
    # Check similarity between 2 cleaned texts using cosine similarity

    # Convert words into frequency vectors
    words1 = text1.split()
    words2 = text2.split()
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # Find set of all unique words
    all_words = set(counter1.keys()).union(set(counter2.keys()))

    # Create frequency vectors
    vec1 = [counter1.get(word, 0) for word in all_words]
    vec2 = [counter2.get(word, 0) for word in all_words]

    # Compute cosine similarity
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  # avoid zero division

    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)

    obama_file = os.path.join(base_path, '..', 'data', 'barrack_obama_speech.txt')
    michelle_file = os.path.join(base_path, '..', 'data', 'michelle_obama_speech.txt')
    trump_file = os.path.join(base_path, '..', 'data', 'donald_trump_speech.txt')
    melania_file = os.path.join(base_path, '..', 'data', 'melania_trump_speech.txt')

    stop_words_file = os.path.join(base_path, '..', 'data', 'stop_words.py')

    # Read speeches
    with open(obama_file, 'r', encoding='utf-8') as f:
        obama_text = f.read()
    with open(michelle_file, 'r', encoding='utf-8') as f:
        michelle_text = f.read()
    with open(trump_file, 'r', encoding='utf-8') as f:
        trump_text = f.read()
    with open(melania_file, 'r', encoding='utf-8') as f:
        melania_text = f.read()

    # Clean texts
    obama_clean = clean_text(obama_text)
    michelle_clean = clean_text(michelle_text)
    trump_clean = clean_text(trump_text)
    melania_clean = clean_text(melania_text)

    # Remove stop words
    obama_filtered = remove_support_words(obama_clean, stop_words_file)
    michelle_filtered = remove_support_words(michelle_clean, stop_words_file)
    trump_filtered = remove_support_words(trump_clean, stop_words_file)
    melania_filtered = remove_support_words(melania_clean, stop_words_file)

    # Check similarity
    similarity_score = check_text_similarity(obama_filtered, trump_filtered)
    print(f'Obama v Trump Speech Similarity: {similarity_score:.2f}')
    similarity_score = check_text_similarity(michelle_filtered, melania_filtered)
    print(f'Michelle v Melania Speech Similarity: {similarity_score:.2f}')
    similarity_score = check_text_similarity(obama_filtered, michelle_filtered)
    print(f'Obama v Michelle Speech Similarity: {similarity_score:.2f}')
    similarity_score = check_text_similarity(trump_filtered, melania_filtered)
    print(f'Trump v Melania Speech Similarity: {similarity_score:.2f}')

# 8: Find the 10 most repeated words in the romeo_and_juliet.txt
print('8:')
def most_common_words_in_file(file_path, n=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Clean the text: remove punctuation and numbers, lowercase everything
    cleaned_text = re.sub(r'[^A-Za-z\s]', '', text).lower()

    # Split into individual words
    words = cleaned_text.split()

    word_counts = Counter(words)
    return word_counts.most_common(n)

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', 'data', 'romeo_and_juliet.txt')

top_10_words = most_common_words_in_file(file_path)
print('Top 10 Most Repeated Words in Romeo and Juliet:')
for word, count in top_10_words:
    print(f'{word}: {count}')

# 9: Read the hacker news csv file and find out:
# A: Count the number of lines containing python or Python
# B: Count the number lines containing JavaScript, javascript or Javascript
# C: Count the number lines containing Java and not JavaScript
print('9:')
def analyse_hacker_news(file_path):

    python_count = 0
    javascript_count = 0
    java_count = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_lower = line.lower()

            if 'python' in line_lower:
                python_count += 1

            if 'javascript' in line_lower:
                javascript_count += 1

            if 'java' in line_lower and 'javascript' not in line_lower:
                java_count += 1

        return python_count, javascript_count, java_count

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, '..', 'data', 'hacker_news.csv')

python_count, javascript_count, java_count = analyse_hacker_news(file_path)
print(f'Lines containing Python/python: {python_count}')
print(f'Lines containing JavaScript/Javascript/javascript: {javascript_count}')
print(f'Lines containing Java/java: {java_count}')


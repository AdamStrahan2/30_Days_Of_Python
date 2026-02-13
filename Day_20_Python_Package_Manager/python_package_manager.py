# ------ Python Package Manager (PIP) ------

# --- What is PIP? ----
# PIP stands for Preferred installer program. We use pip to install different Python packages.
# A Package is a Python module that can contain one or more modules or other packages.
# A module or modules that we can install to our application is a package.
# In programming, we do not have to write every utility program,
# instead we install packages and import them to our applications.

# --- Checking if PIP is Installed ---
# Check if pip is installed by writing:
#pip --version

# --- Installing PIP ---
#  Go to your terminal or command prompt and copy and paste this:
#C:\Users\adams\PycharmProjects\30DaysOfPython> pip install pip

# --- Updating PIP ---
# Go to terminal and run this:
#python.exe -m pip install --upgrade pip

# ------ Installing Packages Using PIP ------

# --- Numpy ---
# Let us try to install numpy, called numeric python.
# It is one of the most popular packages in the machine learning and data science community.
# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
#   - a powerful N-dimensional array object
#   - sophisticated (broadcasting) functions
#   - tools for integrating C/C++ and Fortran code
#   - useful linear algebra, Fourier transform, and random number capabilities

#pip install numpy

# Let us start using numpy. Open your python interactive shell, write python and then import numpy as follows:
# >>> import numpy
# >>> numpy.version.version
# '2.3.4'
# >>> lst = [1, 2, 3, 4, 5]
# >>> np_arr = numpy.array(lst)
# >>> np_arr
# array([1, 2, 3, 4, 5])
# >>> len(np_arr)
# 5
# >>> np_arr * 2
# array([ 2,  4,  6,  8, 10])
# >>> np_arr  + 2
# array([3, 4, 5, 6, 7])
# >>>

# --- Pandas ---
# Pandas is an open source, BSD-licensed library providing high-performance,
# easy-to-use data structures and data analysis tools for the Python programming language.
# Let us install the big brother of numpy, pandas:

#pip install pandas

# >>> import pandas

# --- Webbrowser ---
# Let us import a web browser module, which can help us to open any website.
# We do not need to install this module, it is already installed by default with Python 3.
# For instance if you like to open any number of websites at any time or if you like to schedule something,
# this webbrowser module can be used.
import webbrowser

# list of urls: python
url_lists = [
    'https://www.python.org',
    'https://www.linkedin.com/in/adam-strahan-b6a640193/',
    'https://github.com/AdamStrahan2',
    'https://adamstrahan2.github.io/CV-Adam-Strahan/',
]

# # opens the above list of websites in a different tab
#for url in url_lists:
   # webbrowser.open_new_tab(url)

# ------ Uninstalling Packages ------

# If you do not like to keep the installed packages, you can remove them using the following command:
#pip uninstall packagename

# ------ List Packages ------

# To see the installed packages on our machine, we can use pip followed by list:
# >>> pip list
# Package         Version
# --------------- -----------
# numpy           2.3.4
# pandas          2.3.3
# pip             25.3
# python-dateutil 2.9.0.post0
# pytz            2025.2
# six             1.17.0
# tzdata          2025.2

# ------ Show Package Information ------

# To show information about a package:

# >>>  pip show pandas
# Name: pandas
# Version: 2.3.3
# Summary: Powerful data structures for data analysis, time series, and statistics
# Home-page: https://pandas.pydata.org
# ...

# If we want even more details, just add --verbose:

# >>> pip show --verbose pandas

# ------ PIP Freeze ------

# Generate installed Python packages with their version and the output is suitable to use it in a
# requirements file. A requirements.txt file is a file that should contain all the
# installed Python packages in a Python project:

# >>> pip freeze
# numpy==2.3.4
# pandas==2.3.3
# python-dateutil==2.9.0.post0
# pytz==2025.2
# six==1.17.0
# tzdata==2025.2

# The pip freeze gave us the packages used, installed and their version.
# We use it with requirements.txt file for deployment.

# ------ Reading From URL ------

# By now you are familiar with how to read or write on a file located on the local machine.
# Sometimes, we would like to read from a website using a URL or from an API.
# API stands for Application Program Interface.
# It is a means to exchange structured data between servers primarily as json data.
# To open a network connection, we need a package called requests - it allows to open
# a network connection and to implement CRUD(create, read, update and delete) operations.
# In this section, we will cover only reading ore getting part of a CRUD.

# >>> pip install requests

# We will see get, status_code, headers, text and json methods in requests module:
#   - get(): to open a network and fetch data from url - it returns a response object
#   - status_code: After we fetched data, we can check the status of the operation (success, error, etc)
#   - headers: To check the header types
#   - text: to extract the text from the fetched response object
#   - json: to extract json data
# Let's read a txt file from this website: https://github.com/AdamStrahan2:

import requests
import re
from collections import Counter
import statistics

url = 'https://github.com/AdamStrahan2' # text from a website

response = requests.get(url) # opening a network and fetching a data
print('Response:', response)
print('Response Status Code:', response.status_code) # status code, success:200
print('Response Headers:', response.headers)     # headers information
print('Response Text:', response.text) # gives all the text from the page

# Let us read from an API. API stands for Application Program Interface.
# It is a means to exchange structure data between servers primarily a json data.
# An example of an API: https://pokeapi.co/api/v2/. Let us read this API using requests module.
base_url = 'https://pokeapi.co/api/v2/'  # countries api
response = requests.get(base_url)  # opening a network and fetching a data
print('Pokemon Response:', response) # response object
print('Pokemon Status Code:', response.status_code)  # status code, success:200

def get_pokemon_info(name):
    url = f'{base_url}/pokemon/{name}'
    response = requests.get(url)
    print('Response:', response)
    if response.status_code == 200:
        print(f'Data retrieved for {name}')
        pokemon_data = response.json()  # convert json to python dictionary
        return pokemon_data
    else:
        print(f'Failed to get pokemon info for {name}')
        print(f'Status Code: {response.status_code}')
        return None

pokemon_name = input('Pokemon Name: ')
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f'Pokemon Name: {pokemon_info["name"].capitalize()}')
    print(f'ID: {pokemon_info["id"]}')
    print(f'Weight: {pokemon_info["weight"]}')
    print(f'Height: {pokemon_info["height"]}')
# We use json() method from response object if we are fetching JSON data.
# For txt, html, xml and other file formats we can use text.

# ------ Creating A Package ------

# We organize a large number of files in different folders and sub-folders based on some criteria,
# so that we can find and manage them easily. As you know, a module can contain multiple objects,
# such as classes, functions, etc. A package can contain one or more relevant modules.
# A package is actually a folder containing one or more module files.
# Let us create a package named mypackage, using the following steps:
#   - Create a new folder named mypacakge inside 30DaysOfPython folder.
#   - Create an empty init.py file in the mypackage folder.
#   - Create modules arithmetic.py and greet.py.
# Now let's open the python interactive shell and try the package we have created:

# >>> from mypackage import arithmetic
# >>> arithmetic.add_numbers(1, 2, 3, 5)
# 11
# >>> arithmetic.subtract(5, 3)
# 2
# >>> arithmetic.multiply(5, 3)
# 15
# >>> arithmetic.division(5, 3)
# 1.6666666666666667
# >>> arithmetic.remainder(5, 3)
# 2
# >>> arithmetic.power(5, 3)
# 125
# from mypackage import greet
# greet.greet_person('adam', 'strahan')
# 'Adam Strahan, welcome to 30DaysOfPython Challenge!'
# >>>

# ------ Init.py File ------

# As you can see our package works perfectly. The package folder contains a special file called init.py.
# It stores the package's content. If we put init.py in a package folder, python recognizes it as a package.
# The init.py exposes specified resources from its modules to be imported to other python files.
# An empty init.py file makes all functions available when a package is imported.
# The init.py is essential for the folder to be recognized by Python as a package.

# ------ Extra Package Informatiom ------

# --- Database ---

# SQLAlchemy or SQLObject - Object oriented access to several different database systems
# >>> pip install SQLAlchemy

# --- Web Development ---

# Django - High-level web framework.
# >>> pip install django
# Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
# >>> pip install flask

# --- HTML Parser ---

# Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
# >>> pip install beautifulsoup4
# PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

# --- XML Processing ---

# ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical
# data structures, such as simplified XML infosets, in memory.
# Python 2.5 and up has ElementTree in the Standard Library.

# --- GUI ---

# PyQt - Bindings for the cross-platform Qt framework.
# TkInter - The traditional Python user interface toolkit.

# --- Data Analysis, Data Science and Machine learning ---

# Numpy  - One of the most popular machine learning libraries in Python.
# Pandas - Data analysis, data science and machine learning library in Python that provides
#          data structures of high-level and a wide variety of tools for analysis.
# SciPy  - Machine learning library for application developers and engineers. Contains modules for
#          optimization, linear algebra, integration, image processing, and statistics.
# Scikit-Learn - It is NumPy and SciPy. One of the best libraries for working with complex data.
# TensorFlow   - A machine learning library built by Google.
# Keras        - One of the coolest machine learning libraries in Python. Provides an easier mechanism
#                to express neural networks. Also provides some of the best utilities for compiling models,
#                processing data-sets, visualization of graphs, and much more.

# --- Network ---
#
# requests - A package we can use to send requests to a server(GET, POST, DELETE, PUT)
# >>> pip install requests

# ------ Exercises ------

# 1: Read this url and find the 10 most frequent words. romeo_and_juliet:
#    https://www.gutenberg.org/cache/epub/1513/pg1513.txt
print('1: Romeo & Juliet Top 10 Words')
# Get text from URL
url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
text = requests.get(url).text
# Clean text, remove non-letters, convert to lowercase
cleaned = re.sub(r'[^a-zA-Z\s]', ' ', text).lower()

words = cleaned.split()
word_counts = Counter(words)
top_10_words = word_counts.most_common(10)
for word, count in top_10_words:
    print(f'{word}: {count}')

# 2: Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find:
# A: the min, max, mean, median, standard deviation of cats' weight in metric units.
# B: the min, max, mean, median, standard deviation of cats' lifespan in years.
# C: Create a frequency table of country and breed of cats
print('2:')
cat_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cat_api)
data = response.json()

# Helper functions
def parse_range(value):
    # Convert an 'x - y' string into the average numerical value
    try:
        parts = value.split(' - ')
        parts = [float(p) for p in parts]
        return (parts[0] + parts[1]) / 2
    except:
        return None


# A: Weights (Metrics)
weights = [parse_range(cat['weight']['metric']) for cat in data if cat.get('weight')]
weights = [w for w in weights if w is not None]

# B: Lifespans
lifespans = [parse_range(cat['life_span']) for cat in data if cat.get('life_span')]
lifespans = [l for l in lifespans if l is not None]

# Statistics
def describe(values):
    return {
        'min': min(values),
        'max': max(values),
        'mean': statistics.mean(values),
        'median': statistics.median(values),
        'stdev': statistics.stdev(values),
    }

weight_stats = describe(weights)
life_stats = describe(lifespans)

# C: Frequency table of countries and breeds
country_breeds = Counter(cat.get('origin', 'Unknown') for cat in data)

# Display results
print('Weight (kg) Stats:', weight_stats)
print('Life Span Stats:', life_stats)
print('Frequency of Breeds by Country:')
for country, count in country_breeds.items():
    print(f'{country}: {count}')


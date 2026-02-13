# ------ Pandas ------

# Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python
# programming language. Pandas adds data structures and tools designed to work with table-like data
# which is Series and Data Frames. Pandas provides tools for data manipulation:
# - reshaping
# - merging
# - sorting
# - slicing
# - aggregation
# - imputation. If you are using anaconda, you do not have to install pandas.

# ------ Installing Pandas ------

# pip install conda
# pip install pandas

# Pandas data structure is based on Series and DataFrames.
# A series is a column and a DataFrame is a multidimensional table made up of collection of series.
# In order to create a pandas series we should use numpy to create one dimensional arrays or a python list.

# Pandas series is just one column of data. If we want to have multiple columns we use data frames.
# Data frame is a collection of rows and columns.

# ------ Importing Pandas ------

import pandas as pd
import numpy as np

# ------ Series ------

# --- Creating Pandas Series With Default Index ---

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)

# --- Creating Pandas Series With Custom Index ---

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# --- Creating Pandas Series From A Dictionary ---

dct = {'name':'Adam','country':'Ireland','city':'Carlow'}
s = pd.Series(dct)
print(s)

# --- Creating A Constant Pandas Series ---

s = pd.Series(10, index=[1,2,3])
print(s)

# --- Creating Pandas Series Using Linspace ---

s = pd.Series(np.linspace(5, 20, 10))
print(s)

# ------ DataFrames ------

# --- Creating DataFrames From List Of Lists ---

data = [
    ['Adam', 'Ireland', 'Carlow'],
    ['James', 'UK', 'London'],
    ['Yang', 'China', 'Beijing']
]
df = pd.DataFrame(data, columns=['Name', 'Country', 'City'])
print(df)

# --- Creating DataFrames Using Dictionary ---

data = {'Name': ['Adam', 'James', 'Yang'], 'Country':[
    'Ireland', 'UK', 'China'], 'City': ['Carlow', 'London', 'Beijing']}
df = pd.DataFrame(data)
print(df)

# --- Creating DataFrames Using A List Of Dictionaries ---

data = [
    {'Name': 'Adam', 'Country': 'Ireland', 'City': 'Carlow'},
    {'Name': 'James', 'Country': 'UK', 'City': 'London'},
    {'Name': 'Yang', 'Country': 'China', 'City': 'Beijing'}]
df = pd.DataFrame(data)
print(df)

# ------ Reading CSV File Using Pandas ------

# To download the CSV file, what is needed in this example, console/command line is enough:
# >>> curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv

# Put the downloaded file in your working directory
df = pd.read_csv('weight-height.csv')
print(df)

# ------ Data Exploration ------

# Read only the first 5 rows using head()
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

# Explore the last recordings of the dataframe using the tail() methods.
print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

# As you can see the csv file has three rows: Gender, Height and Weight.
# If the DataFrame had many rows, it would be hard to know all the columns.
# Therefore, we should use the shape method to know the columns. we do not know the number of rows.
print(df.shape) # as you can see 10000 rows and three columns

print(df.columns)  # Index(['Gender', 'Height', 'Weight'], dtype='object')

# Get a specific column using the column key
heights = df['Height']  # This is now a Series
print(heights)

weights = df['Weight']
print(weights)

print(len(heights) == len(weights))  # True

# The describe() method provides descriptive statistical values of a dataset
print('-----Heights-----')
print(heights.describe())
print('-----Weights-----')
print(weights.describe())
print('-----DataFrame-----')
print(df.describe())  # describe can also give statistical information from a dataFrame

# ------ Modifying DataFrames ------

# --- Creating a DataFrame ---

data = [
    {'Name': 'Adam', 'Country': 'Ireland', 'City': 'Carlow'},
    {'Name': 'James', 'Country': 'UK', 'City': 'London'},
    {'Name': 'Yang', 'Country': 'China', 'City': 'Beijing'}]
df = pd.DataFrame(data)
print(df)

# Adding a column to a DataFrame is like adding a key to a dictionary.
# First let's use the previous example to create a DataFrame.
# After we create the DataFrame, we will start modifying the columns and column values.

# --- Adding A New Column ---

weights = [74, 78, 69]
df['Weight'] = weights
print(df)
heights = [173, 175, 169]
df['Height'] = heights
print(df)

# As you can see in the DataFrame above, we did add new columns, Weight and Height. Let's add one additional
# column called BMI(Body Mass Index) by calculating their BMI using their mass and height.
# BMI is mass divided by height squared (in meters) - Weight/Height * Height.
# As you can see, the height is in centimeters, so we should change it to meters. Let's modify the height row.

# --- Modifying Column Values ---

df['Height'] = df['Height'] * 0.01
print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()

df['BMI'] = bmi
print(df)

# --- Formatting DataFrame Columns ---

# The BMI column values of the DataFrame are float with many significant digits after decimal.
# Let's change it to one significant digit after point.
df['BMI'] = round(df['BMI'], 1)
print(df)

birth_year = ['1997', '1981', '1776']
current_year = pd.Series(2026, index=[0, 1, 2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

# --- Checking Data Types Of Column Values ---

print(df.Weight.dtype)
print(df.BMI.dtype)
print(df['Birth Year'].dtype)  # it gives object, we should change this to number
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype)  # int64

df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)

# Now the column values of birth year and current year are integers. We can calculate the age.
ages = df['Current Year'] - df['Birth Year']
print(ages)
df['Age'] = ages
print(df)

# The person in the first row lived so far for 251 years. It is unlikely for someone to live so long.
# Either it is a typo or the data is cooked.
# Let's fill that data with average of the columns without including outlier.
mean = (29 + 45)/2
print('Mean:', mean)  # 37

# --- Boolean Indexing ---

print(df[df['Age'] > 120])
print(df[df['Age'] < 120])

# ------ Exercises ------

# 1: Read the hacker_news.csv file from data directory
print('1:')
hack_file = pd.read_csv('../data/hacker_news.csv')
print(hack_file)

# 2: Get the first five rows
print('2:')
print(hack_file.head())

# 3: Get the last five rows
print('3:')
print(hack_file.tail())

# 4: Get the title column as pandas series
print('4:')
titles = hack_file['title']
print(titles)
print(type(titles))
print(titles.head())

# 5: Count the number of rows and columns.
print('5:')
num_rows, num_cols = hack_file.shape
print('Rows:', num_rows)
print('Columns:', num_cols)

# 5A: Filter the titles which contain python
print('5A:')
python_titles = hack_file[hack_file['title'].str.contains('python', case=False, na=False)]
print(python_titles)

# 5B: Filter the titles which contain JavaScript
print('5B:')
javascript_titles = hack_file[hack_file['title'].str.contains('javascript', case=False, na=False)]
print(javascript_titles)

# 5C: Explore the data and make sense of it
print('5C:')
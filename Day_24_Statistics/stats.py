# ------ Statistics ------

# Statistics is the discipline that studies the collection, organization, displaying, analysing,
# interpretation and presentation of data. Statistics is recommended to be a prerequisite for data science
# and machine learning. Statistics is a very broad field but we will focus only on the most relevant part.
# After this challenge, you may go to the web development, data analysis, machine learning and data science path.
# Whatever path you take, at some point in your career you will get data which you may work on.
# Having some statistical knowledge will help you to make decisions based on data.

# ------ Data ------

# Data is any set of characters that is gathered and translated for some purpose, usually analysis.
# It can be any character, including text and numbers, pictures, sound, or video.
# If data is not put in a context, it doesn't make any sense to a human or computer.
# To make sense from data we need to work on the data using different tools.
# The work flow of data analysis, data science or machine learning starts from data.
# Data can be provided from some data source or it can be created. There is structured and unstructured data.
# Data can be found in small or big format. Most of the data types we will get have been covered
# in the file handling section.

# ------ Statistics Module ------

# The Python statistics module provides functions for calculating mathematical statistics of numerical data.
# The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy,
# or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS
# and Matlab. It is aimed at the level of graphing and scientific calculators.

# ------ NumPy ------

# In the first section we defined Python as a great general-purpose programming language on its own,
# but with the help of other popular libraries (numpy, scipy, matplotlib, pandas etc) it becomes a powerful
# environment for scientific computing.
# NumPy is the core library for scientific computing in Python. It provides a high-performance
# multidimensional array object, and tools for working with arrays.
# So far, we have been using vscode but from now on I would recommend using Jupyter Notebook.
# To access jupyter notebook let's install anaconda. If you are using anaconda most of the common packages
# are included and you don't have to install packages if you installed anaconda.

# PS C:\Users\adams\PycharmProjects\30DaysOfPython> pip install numpy

# ------ Importing NumPy ------

import numpy as np

# How to check the version of the numpy package
print('numpy:', np.__version__)

# Checking the available methods
print(dir(np))

# ------ Creating NumPy Arrays ------

# --- Int ---
# Create python list
python_list = [1, 2, 3, 4, 5]
# Checking Data Types
print('Type:', type(python_list))  # Type: <class 'list'>
print('python_list:', python_list)  # python_list: [1, 2, 3, 4, 5]

two_d_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print('two_d_list:', two_d_list)  # two_d_list: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list_int = np.array(python_list)
print('Type:', type(numpy_array_from_list_int))  # Type: <class 'numpy.ndarray'>
print('numpy_array_from_list_int:', numpy_array_from_list_int)  # numpy_array_from_list_int: [1 2 3 4 5]

# --- Float ---
# Create python list
python_list = [1, 2, 3, 4, 5]
numpy_array_from_list_float = np.array(python_list, dtype=float)
print('numpy_array_from_list_float:', numpy_array_from_list_float)  # numpy_array_from_list_float: [1. 2. 3. 4. 5.]

# --- Boolean ---
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False, True, True, False, False])

# --- Multi-Dimensional Array ---
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))  # <class 'numpy.ndarray'>
print(numpy_two_dimensional_list)  # [[0 1 2][3 4 5][6 7 8]]

# --- Converting Array To List ---
# We can always convert an array back to a python list using tolist()
np_to_list = numpy_array_from_list_int.tolist()
print('Type:', type(np_to_list))  # Type: <class 'list'>
print('1D Array:', np_to_list)  # 1D Array: [1, 2, 3, 4, 5]
print('2D Array:', numpy_two_dimensional_list.tolist())  # 2D Array: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# --- Array From Tuple ---
python_tuple = (1, 2, 3, 4, 5)
print('Type:', type(python_tuple))  # Type: <class 'tuple'>
print('Tuple:', python_tuple)  # Tuple: (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print('Type:', type(numpy_array_from_tuple))  # Type: <class 'numpy.ndarray'>
print('numpy_array_from_tuple:', numpy_array_from_tuple)  # numpy_array_from_tuple: [1 2 3 4 5]

# --- Shape of Numpy Array ---
# The shape method provide the shape of the array as a tuple. The first is the row and the second is the column.
# If the array is just one dimensional it returns the size of the array.
nums = np.array([1, 2, 3, 4, 5])
print(nums)  # [1 2 3 4 5]
print('Shape of nums:', nums.shape)  # Shape of nums: (5,)
print(numpy_two_dimensional_list)  # [[0 1 2], [3 4 5], [6 7 8]]
print('Shape of numpy_two_dimensional_list:', numpy_two_dimensional_list.shape)  # Shape of numpy_two_dimensional_list: (3, 3)
three_by_four_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(three_by_four_array)  # [[ 0  1  2  3], [ 4  5  6  7], [ 8  9 10 11]]
print('Shape of three_by_four_array:', three_by_four_array.shape)  # Shape of three_by_four_array: (3, 4)

# --- Data Type of Array ---
# Type of data types: str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)  # [-3 -2 -1  0  1  2  3]
print(int_array.dtype)  # int64
print(float_array)  # [-3. -2. -1.  0.  1.  2.  3.]
print(float_array.dtype)  # float64

# --- Size of Array ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print('list size:', numpy_array_from_list.size)  # list size: 5
print('2D list size:', two_dimensional_list.size)  # 2D list size: 9

# ------ Mathematical Operations Using Numpy ------

# NumPy array is not like exactly like python list. To do mathematical operation in Python list we
# have to loop through the items but numpy can allow to do any mathematical operation without looping.

# --- Addition ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('Array:', numpy_array_from_list)  # Array: [1 2 3 4 5]
ten_plus_array = numpy_array_from_list + 10
print('Ten plus array:', ten_plus_array)  # Ten plus array: [11 12 13 14 15]

# --- Subtraction ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('Array:', numpy_array_from_list)  # Array: [1 2 3 4 5]
ten_minus_array = numpy_array_from_list - 10
print('Ten minus array:', ten_minus_array)  # Ten minus array: [-9 -8 -7 -6 -5]

# --- Multiplication ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('Array:', numpy_array_from_list)  # Array: [1 2 3 4 5]
ten_times_array = numpy_array_from_list * 10
print('Ten times array:', ten_times_array)  # Ten times array: [10 20 30 40 50]

# --- Division ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('Array:', numpy_array_from_list)  # Array: [1 2 3 4 5]
ten_divide_array = numpy_array_from_list / 10
print('Ten divide array:', ten_divide_array)  # Ten divide array: [0.1 0.2 0.3 0.4 0.5]

# --- Modulus ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('Array:', numpy_array_from_list)  # Array: [1 2 3 4 5]
mod_three_array = numpy_array_from_list % 3
print('Mod 3 array:', mod_three_array)  # Mod 3 array: [1 2 0 1 2]

# --- Floor Division ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('Array:', numpy_array_from_list)  # Array: [1 2 3 4 5]
floor_div_array = numpy_array_from_list // 10
print('Floor division array:', floor_div_array)  # Floor division array: [0 0 0 0 0]

# --- Exponential ---
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('Array:', numpy_array_from_list)  # Array: [1 2 3 4 5]
squared_array = numpy_array_from_list ** 2
print('Squared array:', squared_array)  # Squared array: [ 1  4  9 16 25]

# ------ Checking Data Types ------

numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr.dtype)  # int64
print(numpy_float_arr.dtype)  # float64
print(numpy_bool_arr.dtype)  # bool

# ------ Converting Data Types ------

# --- Int to Float ---
numpy_int_arr = np.array([1, 2, 3, 4], dtype = 'float')
print(numpy_int_arr)  # [1. 2. 3. 4.]

# --- Float to Int ---
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)  # [1 2 3 4]

# --- Int to Boolean ---
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_bool_arr)  # [False  True  True False False]

# --- Int to String ---
numpy_float_list = np.array([1., 2., 3., 4.])
numpy_float_list = numpy_float_list.astype('int').astype('str')
print(numpy_float_list)  # ['1' '2' '3' '4']

# ------ Multi-Dimensional Arrays ------

two_d_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_d_array))  # <class 'numpy.ndarray'>
print(two_d_array)  # [[1 2 3][4 5 6][7 8 9]]
print('Shape:', two_d_array.shape)  # Shape: (3, 3)
print('Size:', two_d_array.size)  # Size: 9
print('Data Type:', two_d_array.dtype)  # Data Type: int64

# ------ Getting Items From Numpy Array ------

first_row = two_d_array[0]
second_row = two_d_array[1]
third_row = two_d_array[2]
print('First row:', first_row)  # First row: [1 2 3]
print('Second row:', second_row)  # Second row: [4 5 6]
print('Third row:', third_row)  # Third row: [7 8 9]

first_column = two_d_array[:,0]
second_column = two_d_array[:,1]
third_column = two_d_array[:,2]
print('First column:', first_column)  # First column: [1 4 7]
print('Second column:', second_column)  # Second column: [2 5 8]
print('Third column:', third_column)  # Third column: [3 6 9]
print(two_d_array)

# ------ Slicing Numpy Array ------

first_two_rows_and_columns = two_d_array[0:2, 0:2]
print('First two rows and columns:', first_two_rows_and_columns)  # First two rows and columns: [[1 2][4 5]]

# ------ Reversing Positions ------

# --- Reversed Rows ---
reversed_rows = two_d_array[::-1]
print('Reversed rows:', reversed_rows)

# --- Reversed Rows and Columns
reversed_rows_and_columns = two_d_array[::-1, ::-1]
print('Reversed rows and columns:', reversed_rows_and_columns)

# ------ Representing Missing Values ------

# --- Substitutions ---
two_d_with_subs = two_d_array
print('Array:', two_d_with_subs)
two_d_with_subs[1, 1] = 55
two_d_with_subs[2, 2] = 44
print('Array with Subs:', two_d_with_subs)  # Array with Subs: [[ 1  2  3][ 4 55  6][ 7  8 44]]

# --- Numpy Zeroes ---
numpy_zeroes = np.zeros((3,3), dtype='int', order='C')
print(numpy_zeroes)  # [[0 0 0][0 0 0][0 0 0]]

# --- Numpy Ones ---
numpy_ones = np.ones((4,4), dtype='int', order='C')
print(numpy_ones)  # [[1 1 1 1][1 1 1 1][1 1 1 1][1 1 1 1]]

twos = numpy_ones * 2
print(twos)  # [[2 2 2 2][2 2 2 2][2 2 2 2][2 2 2 2]]

# --- Reshape ---
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)  # [[1 2 3][4 5 6]]
reshaped = first_shape.reshape(3,2)
print(reshaped)  # [[1 2][3 4][5 6]]
flattened = reshaped.flatten()
print(flattened)  # [1 2 3 4 5 6]

# --- Horizontal Stack ---
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)  # [5 7 9]
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))  # Horizontal Append: [1 2 3 4 5 6]

# --- Vertical Stack ---
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))  # Vertical Append: [[1 2 3][4 5 6]]

# ------ Generating Random Numbers ------

# --- Random Floats ---
random_float = np.random.random()
print(random_float)  # 0.3543329957549969
random_floats = np.random.random(5)
print(random_floats)  # [0.97176932 0.60849721 0.05602579 0.38686812 0.71972708]

# --- Random Ints From 0-10 ---
random_int = np.random.randint(0, 11)
print('Random Int 0-10:', random_int)  # Random Int 0-10: 4

# --- Random Ints 2-10, Creating A One Row Array ---
random_int = np.random.randint(2,11, size=4)
print('Random Int 2-10:', random_int)  # Random Int 2-10: [5 5 9 3]

# --- Random Multi-Dimensional Array ---
random_array = np.random.randint(0,11, size=(3,3))
print('Random Array:', random_array)  # Random Array: [[4 8 5][5 9 1][7 1 9]]

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print('Normal Array:', normal_array)

# ------ Numpy And Statistics ------

import matplotlib.pyplot as plt
import seaborn as sns

a_set = sns.set()
a_hist_plot = plt.hist(normal_array, color='grey', bins=50)
print(a_set)
print(a_hist_plot)

# ------ Matrix In Numpy ------

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)  # [[1. 1. 1. 1.][1. 1. 1. 1.][1. 1. 1. 1.][1. 1. 1. 1.]]

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)  # [[1. 1. 1. 1.][1. 1. 1. 1.][2. 2. 2. 2.][1. 1. 1. 1.]]

# ------ Numpy Arange() ------

# Sometimes you want to create values that are evenly spaced within a defined interval.
# For instance, you want to create values from 1 to 10; you can use numpy.arange() function
# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
for l in lst:
    print(l)  # 0 2 4 6 8 10

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)  # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)  # [ 1  3  5  7  9 11 13 15 17 19]

even_numbers = np.arange(2, 20, 2)
print(even_numbers)  # [ 2  4  6  8 10 12 14 16 18]

# ------ Create A Sequence Of Numbers With Linspace ------

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
seq = np.linspace(1.0, 5.0, num=10)
print(seq)  # [1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222 3.66666667 4.11111111 4.55555556 5.        ]

# Don't include the last value in the interval
seq = np.linspace(1.0, 5.0, num=5, endpoint=False)
print(seq)  # [1.  1.8 2.6 3.4 4.2]

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# numpy.logspace(start, stop, num, endpoint)
log = np.logspace(2, 4.0, num=4)
print(log)  # [  100.           464.15888336  2154.43469003 10000.        ]

# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
print(x)  # [1.+0.j 2.+0.j 3.+0.j]
print(type(x))  # <class 'numpy.ndarray'>
print(x.size)  # 3
print(x.itemsize)  # 16

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)
print('First row: ', np_list[0])  # First row:  [1 2 3]
print('Second row: ', np_list[1])  # Second row:  [4 5 6]
print('First column: ', np_list[:,0])  # First column:  [1 4]
print('Second column: ', np_list[:,1])  # Second column:  [2 5]
print('Third column: ', np_list[:,2])  # Third column:  [3 6]

# ------ Numpy Statistical Functions ------

# NumPy has quite useful statistical functions for finding minimum, maximum, mean, median, percentile,
# standard deviation and variance, etc from the given elements in the array.
np_normal_dis = np.random.normal(5, 0.5, 100)
print('np_normal_dis:', np_normal_dis)
print('two_d_array:', two_d_array)  # two_d_array: [[ 1  2  3][ 4 55  6][ 7  8 44]]

# min, max, mean, median, sd
print('min:', two_d_array.min())  # min: 1
print('max:', two_d_array.max())  # max: 55
print('mean:',two_d_array.mean())  # mean: 14.444444444444445
#print('median: ', two_d_array.median())
print('sd:', two_d_array.std())  # sd: 19.038622213870127

print(two_d_array)
print('Column with minimum: ', np.amin(two_d_array,axis=0))  # Column with minimum:  [1 2 3]
print('Column with maximum: ', np.amax(two_d_array,axis=0))  # Column with maximum:  [ 7 55 44]
print('=== Row ==')
print('Row with minimum: ', np.amin(two_d_array,axis=1))  # Row with minimum:  [1 4 7]
print('Row with maximum: ', np.amax(two_d_array,axis=1))  # Row with maximum:  [ 3 55 44]

# --- Repeating ---

a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:', np.tile(a, 2))  # Tile: [1 2 3 1 2 3]

# Repeat each element of 'a' two times
print('Repeat:', np.repeat(a, 2))  # Repeat: [1 1 2 2 3 3]

# --- Random ---

# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)  # 0.8293144288750706

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)  # [[0.99268356 0.70637227 0.18099757][0.44431778 0.97493693 0.55059064]]

# Random Letters From Choice
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))  # ['a' 'a' 'o' 'i' 'e' 'e' 'u' 'u' 'o' 'e']

# Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)  # [[0.49507489 0.13362751][0.46209256 0.96053697]]

# Natural numbers
rand2 = np.random.randn(2,2)
print(rand2)  # [[-0.19693487  0.75051224][-2.59206327 -0.4031368 ]]

# Random integers between [0, 10) of shape 5,3
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)  # [[6 1 8][2 3 8][1 4 5][5 5 7][2 5 7]]

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
print('np_normal_dis:', np_normal_dis)

## min, max, mean, median, sd
print('min:', np.min(np_normal_dis))  # min: 3.3150785765026027
print('max:', np.max(np_normal_dis))  # max: 6.577512272524464
print('mean:', np.mean(np_normal_dis))  # mean: 5.00218675077842
print('median:', np.median(np_normal_dis))  # median: 5.015308402470824
print('mode:', stats.mode(np_normal_dis))  # mode: ModeResult(mode=np.float64(3.3150785765026027), count=np.int64(1))
print('sd:', np.std(np_normal_dis))  # sd: 0.48960742067521784

# Make a graph
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot
# numpy.dot(x, y, out=None)

# --- Linear Algebra ---

# Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
# (1*4) + (2*5) + (3*3)
print(np.dot(f, g))  # 23

# --- Matrix Multiplication ---

# Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
# [1,2] [5,6]
# [3,4] [7,8]
# (1*5) + (2*7) = 19
# (1*6) + (2*8) = 22
# (3*5) + (4*7) = 43
# (5*4) + (6*8) = 50
print(np.matmul(h, i))  #[[19 22][43 50]]

# Determinant 2*2 matrix
# 5*8-7*6np.linalg.det(i)
print(np.linalg.det(i))  # -2.000000000000005

z = np.zeros((8,8))
z[1::2,::2] = 1
z[::2,1::2] = 1
print(z)

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

np_arr = np.array(range(0, 11))
print(np_arr + 2)  # [ 2  3  4  5  6  7  8  9 10 11 12]

# We use linear equation for quantities which have linear relationship
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)  # [ 7  9 11 13 15]

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

# To draw the Gaussian normal distribution using numpy.
# As you can see below, the numpy can generate random numbers. To create random sample,
# we need the mean(mu), sigma(standard deviation), number of data points.
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.histplot(x, kde=True)
ax.set(xlabel="x", ylabel='y')
plt.show()

# To summarize, the main differences with python lists are:
#
# Arrays support vectorized operations, while lists don’t.
# Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
# Every array has one and only one dtype. All items in it should be of that dtype.
# An equivalent numpy array occupies much less space than a python list of lists.
# numpy arrays support boolean indexing.
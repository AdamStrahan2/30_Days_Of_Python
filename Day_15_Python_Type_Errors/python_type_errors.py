# ------ Python Type Errors ------

# If our code fails to run, the Python interpreter will display a message,
# containing feedback with information on where the problem occurs and the type of an error.
# It will also sometimes gives us suggestions on a possible fix.
# Let us see the most common error types one by one. First let us open our Python interactive shell.
# Go to your you computer terminal and write 'python'. The python interactive shell will be opened.

# ------ SyntaxError ------

# >>> print 'Hello World!'
#   File "<python-input-0>", line 1
#     print 'Hello World!'
#     ^^^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>>

# ------ NameError ------

# >>> print(age)
# Traceback (most recent call last):
#   File "<python-input-1>", line 1, in <module>
#     print(age)
#           ^^^
# NameError: name 'age' is not defined
# >>>

# ------ IndexError ------

# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     numbers[5]
#     ~~~~~~~^^^
# IndexError: list index out of range
# >>>

# ------ ModuleNotFoundError ------

# >>> import maths
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     import maths
# ModuleNotFoundError: No module named 'maths'
# >>> import math

# ------ AttributeError ------

# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<python-input-9>", line 1, in <module>
#     math.PI
# AttributeError: module 'math' has no attribute 'PI'
# >>> math.pi
# 3.141592653589793
# >>>

# ------ KeyError ------

# >>> users = {'name':'Adam', 'age':28, 'country':'Ireland'}
# >>> users['name']
# 'Adam'
# >>> users['job']
# Traceback (most recent call last):
#   File "<python-input-13>", line 1, in <module>
#     users['job']
#     ~~~~~^^^^^^^
# KeyError: 'job'
# >>>

# ------ TypeError ------

# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<python-input-14>", line 1, in <module>
#     4 + '3'
#     ~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>>
# >>> 4 + int('3')
# 7
# >>>

# ------ ImportError ------

# >>> from math import power
# Traceback (most recent call last):
#   File "<python-input-16>", line 1, in <module>
#     from math import power
# ImportError: cannot import name 'power' from 'math' (unknown location)
# >>>
# >>> from math import pow
# >>> pow(2, 3)
# 8.0
# >>>

# ------ ValueError ------

# >>> int('12a')
# Traceback (most recent call last):
#   File "<python-input-19>", line 1, in <module>
#     int('12a')
#     ~~~^^^^^^^
# ValueError: invalid literal for int() with base 10: '12a'
# >>>

# ------ ZeroDivisionError ------

# >>> 10 / 0
# Traceback (most recent call last):
#   File "<python-input-20>", line 1, in <module>
#     10 / 0
#     ~~~^~~
# ZeroDivisionError: division by zero
# >>> 
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Adam'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Adam'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Find Euclidean distance between (2,3) and (10,8) : d = square root of (x2 - x1)^2 + (y2 - y1)^2
x2 = 10
x1 = 2
y2 = 8
y1 = 3
answer = 0
# Use **2 to square a number
# Use **0.5 to square root a number
answer = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("Distance from (2,3) to (10,8): " + str(answer)) # Convert to String with str()

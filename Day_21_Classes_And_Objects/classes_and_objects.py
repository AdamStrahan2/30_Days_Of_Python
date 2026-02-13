# ------ Classes and Objects ------

# Python is an object-oriented programming language.
# Everything in Python is an object, with its properties and methods.
# A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding built-in class.
# A class is like an object constructor, or a "blueprint" for creating objects.
# We instantiate a class to create an object.
# The class defines attributes and the behavior of the object, while the object represents the class.
# Every element in a Python program is an object of a class. Let us check if everything in python is a class:

# >>> num = 10
# >>> type(num)
# <class 'int'>
# >>> string = 'string'
# >>> type(string)
# <class 'str'>
# >>> boolean = True
# >>> type(boolean)
# <class 'bool'>
# >>> lst = []
# >>> type(lst)
# <class 'list'>
# >>> tpl = ()
# >>> type(tpl)
# <class 'tuple'>
# >>> set1 = set()
# >>> type(set1)
# <class 'set'>
# >>> dct = {}
# >>> type(dct)
# <class 'dict'>

# ------ Creating A Class ------

# To create a class we need the key word class followed by the name and colon. Class name should be CamelCase.
class Person:
    pass
print('Person:', Person)  # Person: <class '__main__.Person'>

# ------ Creating An Object ------

adam = Person()
print('adam:', adam)  # adam: <__main__.Person object at 0x000001E34D9B6900>

# ------ Class Constructor ------

# In the examples above, we have created an object from the Person class.
# However, a class without a constructor is not really useful in real applications.
# Let us use a constructor function to make our class more useful.
# Like the constructor function in Java or JavaScript, Python has also a built-in init() constructor function.
# The init constructor function has self parameter which is a reference to the current instance of the class:
class Person:
    def __init__(self, name):
        # self allows us to attach the parameter to the class
        self.name = name


p = Person('Adam')
print('name:', p.name)  # name: Adam
print(p)  # <__main__.Person object at 0x00000184362C6A50>

#  Let us add more parameters to the constructor function.
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Adam', 'Strahan', 28, 'Ireland', 'Carlow')
print('First Name:', p.firstname)
print('Last Name:', p.lastname)
print('Age:', p.age)
print('Country:', p.country)
print('City:', p.city)

# ------ Object Methods ------

# Objects can have methods. The methods are functions which belong to the object.
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p = Person('Adam', 'Strahan', 28, 'Ireland', 'Carlow')
print(p.person_info())

# ------ Object Default Methods ------

# Sometimes you may want to have a default values for your object methods.
# If we give default values for the parameters in the constructor, we can avoid errors when we call
# or instantiate our class without parameters. Let's see how it looks:
class Person:
    def __init__(self, firstname='Adam', lastname='Strahan', age=28, country='Ireland', city='Carlow'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'


p1 = Person()
print('p1:', p1.person_info())
p2 = Person('John', 'Wick', 50, 'Canada', 'Toronto')
print('p2:', p2.person_info())

# ------ Method To Modify Class Default Values ------

# In the example below, the person class, all the constructor parameters have default values.
# In addition to that, we have skills parameter, which we can access using a method.
# Let us create the add_skill method to add skills to the skills list:
class Person:
    def __init__(self, firstname='Adam', lastname='Strahan', age=28, country='Ireland', city='Carlow'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person()
print('p1:', p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print('p2:', p2.person_info())
print('p1 skills:', p1.skills)
print('p2 skills:', p2.skills)

# ------ Inheritance ------

# Using inheritance we can reuse a parent class code.
# Inheritance allows us to define a class that inherits all the methods and properties from a parent class.
# The parent/super/base class is the class which gives all the methods and properties.
# Child class is the class that inherits from another or parent class.
# Let us create a student class by inheriting from person class:
class Student(Person):
    pass


s1 = Student('Bob', 'Ross', 70, 'Denmark', 'Copenhagen')
s2 = Student('William', 'Windsor', 58, 'England', 'London')
print('s1 info:', s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print('s1 skills:', s1.skills)

print('s2 info:', s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print('s2 skills:', s2.skills)

# We did not call the init() constructor in the child class. We can still access all the properties from the parent.
# But if we do call the constructor we can access the parent properties by calling super. We can add a new
# method to the child or override the parent class methods by creating the same method name in the child class.
# When we add the init() function, the child class will no longer inherit the parent's init() function.

# ------ Overriding Parent Method ------

class Student(Person):
    def __init__ (self, firstname='Adam', lastname='Strahan',age=28, country='Ireland', city='Carlow', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Bob', 'Ross', 70, 'Denmark', 'Copenhagen', gender='male')
s2 = Student('Elizabeth', 'Windsor', 108, 'England', 'London', gender='female')
print('s1 info:', s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print('s1 skills:', s1.skills)

print('s2 info:', s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print('s2 skills:', s2.skills)
# We can use super() built-in function or the parent name Person to automatically inherit the methods
# and properties from its parent. In the example above we override the parent method. The child method
# has a different feature, it can identify, if the gender is male or female and assign the proper pronoun.

# ------ Exercises ------

# 1: Python has the module called statistics. We can use this module to do all the statistical calculations.
# However, to learn how to make function and reuse function let us try to develop a program, which calculates
# the measure of central tendency of a sample (mean, median, mode) and measure of variability
# (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile,
# and frequency distribution of the sample. You can create a class called Statistics and create all the
# functions that do statistical calculations as methods for the Statistics class.
print('1:')
class Statistics:
    def __init__ (self, data):
        if not isinstance(data, list):
            raise TypeError('Data must be a list.')
        if len(data) == 0:
            raise ValueError('Data must not be empty.')
        self.data = sorted(data)

    # Central Tendency
    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]

    def mode(self):
        from collections import Counter
        freq = Counter(self.data)
        max_count = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_count]

        # if all values appear once -> no true mode
        if len(modes) == len(set(self.data)):
            return None
        return modes if len(modes) > 1 else modes[0]

    # Variability
    def data_range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        mean_value = self.mean()
        return sum((x - mean_value) ** 2 for x in self.data) / len(self.data)

    def std(self):
        return self.variance() ** 0.5

    # Other measures
    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)

    def count(self):
        return len(self.data)

    def percentile(self, p):
        # returns pth percentile (0-100)
        if not 0 <= p <= 100:
            raise ValueError('Percentile must be between 0 and 100.')

        k = (len(self.data) - 1) * (p / 100)
        f = int(k)
        c = f + 1

        if c >= len(self.data):
            return self.data[f]

        # Linear interpolation
        return self.data[f] + (self.data[c] - self.data[f]) * (k - f)

    def frequency_distribution(self):
        from collections import Counter
        return dict(Counter(self.data))

    # Display Stats
    def summary(self):
        return {
            'count': self.count(),
            'mean': self.mean(),
            'median': self.median(),
            'mode': self.mode(),
            'minimum': self.minimum(),
            'maximum': self.maximum(),
            'range': self.data_range(),
            'variance': self.variance(),
            'standard_deviation': self.std(),
            '25th_percentile': self.percentile(25),
            '50th_percentile': self.percentile(50),
            '75th_percentile': self.percentile(75),
            'frequency_distribution': self.frequency_distribution()
        }

sample = [2, 5, 9, 5, 7, 2, 5, 10, 3]
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats_sample = Statistics(sample)
stats_ages = Statistics(ages)

print("Sample Statistics:")
for key, value in stats_sample.summary().items():
    print(f"{key}: {value}")

print("Ages Statistics:")
for key, value in stats_ages.summary().items():
    print(f"{key}: {value}")

# 2: Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties
# and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
# Incomes is a set of incomes and its description. The same goes for expenses.
print('2:')
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        # Store incomes/expenses as dictionaries: {'salary': 3000, 'bonus': 500}
        self.income = {}
        self.expenses = {}

    # Add income/expense
    def add_income(self, description, amount):
        # Add income with description
        if amount <= 0:
            raise ValueError('Income must be positive.')
        self.income[description] = self.income.get(description, 0) + amount

    def add_expense(self, description, amount):
        if amount <= 0:
            raise ValueError('Expense must be positive.')
        self.expenses[description] = self.expenses.get(description, 0) + amount

    # Totals
    def total_income(self):
        return sum(self.income.values())

    def total_expense(self):
        return sum(self.expenses.values())

    # Account Balance
    def account_balance(self):
        return self.total_income() - self.total_expense()

    # Info Summary
    def account_info(self):
        info = (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: {self.total_income()}\n"
            f"Total Expense: {self.total_expense()}\n"
            f"Account Balance: {self.account_balance()}\n\n"
            f"Incomes:\n"
        )

        for description, amount in self.income.items():
            info += f" - {description}: {amount}\n"

        info += "\nExpenses:\n"
        for description, amount in self.expenses.items():
            info += f" - {description}: {amount}\n"

        return info

person = PersonAccount("John", "Doe")

person.add_income("Salary", 3000)
person.add_income("Bonus", 500)
person.add_expense("Rent", 1200)
person.add_expense("Groceries", 350)
person.add_expense("Internet", 60)

print(person.account_info())


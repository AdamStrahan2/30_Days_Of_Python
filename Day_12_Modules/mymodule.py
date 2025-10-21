# ------ Modules ------
# A module is a file containing a set of codes or a set of functions which can be included to an application.
# A module could be a file containing a single variable, a function or a big code base.

# ------ Creating Modules ------

# To create a module we write our codes in a python script and we save it as a .py file.
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname


def sum_two_nums(num1, num2):
    return num1 + num2


person = {
    'first_name': 'Adam',
    'last_name': 'Strahan',
    'age': 28,
    'country': 'Ireland',
    'is_married': False,
    'skills': ['JavaScript', 'Java', 'SQL', 'HTML', 'Python'],
    'address': {
        'street': 'Easy Street',
        'zipcode': '90210'
    }
}

gravity = 9.81

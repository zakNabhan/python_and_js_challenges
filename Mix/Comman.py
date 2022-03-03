# this file contains differents Tasks


'''
Create a function which returns the Modulo of the two given numbers.
'''


def mod(param1, param2):
    """
    :param param1:
    :param param2:
    :return:
    """
    return param1 % param2


print(mod(-13, 64))
print(mod(50, 25))
print(mod(-1, 64))

# other version
mod = lambda m, n: m % n

'''
Write two functions:

to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string.

'''


def to_int(txt):
    """
    :param txt:
    :return:
    """
    return int(txt)


def to_str(num):
    """
    :param num:
    :return:
    """
    return str(num)


to_int("77")

to_int("532")

to_str(77)

to_str(532)

# 1 >
# Is the Number Less than or Equal to Zero?
'''
Create a function that takes a number as
its only argument and returns True if
it's less than or equal to zero, otherwise return False.
'''


def less_than_or_equal_to_zero(num):
    """

    :param num:
    :return:
    """
    if num == 0 or num < 0:
        return True
    else:
        return False


# other version


def less_than_or_equal_to_zero(num):
    return num <= 0


'''print(less_than_or_equal_to_zero(5))
print(less_than_or_equal_to_zero(0))
print(less_than_or_equal_to_zero(-23))'''

# 2 >
# Are the Numbers Equal?

'''
Create a function that returns True when num1 is equal to num2; 
otherwise return False.
'''


def is_same_num(num1, num2):
    if num1 == num2:
        return True
    else:
        return False


'''
other version
'''


def is_same_num(num1, num2):
    return num1 == num2


print(is_same_num(3, 5))

# 3 >
# Are the Numbers Equal?

'''

Create a function that takes two numbers as arguments and return their sum.


'''


def addtion(number1, number2):
    """
    :param number1:
    :param number2:
    :return:
    """
    return number1 + number2


# other version
def addition(a, b):
    return sum((a, b))


print(addtion(3, 2))
print(addtion(-3, -6))
print(addtion(7, 3))

'''
Create a function that takes a string and returns it as an integer.
'''


def string_int(param):
    """
    :param param:
    :return:
    """
    return int(param)


string_int('6')
string_int('1000')
string_int('12')

# 2 >
# return the first element in a list
'''
Create a function that takes a list and returns the first element.
'''


def get_first_value(liste=None):
    """
    :param liste:
    :return:
    """
    if liste is None:
        liste = []
    return liste[0]


print(get_first_value([1, 2, 3]))
print(get_first_value([80, 2, 3]))
print(get_first_value([-500, 2, 3]))

'''
Write a function that returns the string
 "something" joined with a space 
" " and the given argument a.'''


def give_me_something(a):
    """

    :param a:
    :return:
    """
    return '"{}"'.format(a)


print(give_me_something("is better than nothing"))
print(give_me_something("Bob Jane"))
print(give_me_something("something"))

'''
Given two numbers, 
return True if the sum of both numbers is less than 100.
 Otherwise return False.


'''


def less_than_100(num1, num2):
    """
    :param num1:
    :param num2:
    :return:
    """
    summe = num1 + num2
    if summe < 100:
        return True
    else:
        return False


print(less_than_100(22, 15))
print(less_than_100(83, 34))
print(less_than_100(3, 77))


def hello_name(name):
    return "Hello {}".format(name)


print(hello_name("Gerald"))

'''
Check if an Integer is Divisible By Five
Create a function that returns True if 
an integer is evenly divisible by 5, and False otherwise.
'''


def divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False


print(divisible_by_five(5))
print(divisible_by_five(-55))
print(divisible_by_five(37))

print("************************************")

import re

text = "the rain in Spanin"

x = re.findall("a", text)
print(x)

txt = "The rain in Spain"
x = re.split(" ", txt)
print(x)



## json

import json
#some json data
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse json data (x)
y = json.loads(x)
print(y)
print(y["age"])
print("************************************")


# Convert from Python to Json

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))

print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

x = lambda a, b: a + b
print(x(23, 4))


def myfunction(n):
    return lambda a, t: (t + a) * n

num1 = myfunction(4)
print(num1(1, 3))

print("______________")

x = ascii("My name is Ståle")
print(x)
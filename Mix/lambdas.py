"""
First Example

Here are a few examples to give you an appetite for some Python code, functional style.

The identity function, a function that returns its argument, is expressed with a standard Python function definition using the keyword def as follows:

>>> def identity(x):
...     return x

identity() takes an argument x and returns it upon invocation.

In contrast, if you use a Python lambda construction, you get the following:

"""

"""
In contrast, if you use a Python lambda construction, you get the following:

>>> lambda x: x

In the example above, the expression is composed of:

    The keyword: lambda
    A bound variable: x
    A body: x
"""

x = lambda x :x + 1 * (3)

print(x(1))


# lambda get fullname

full_name = lambda firstname, lastname:  f"{firstname} , {lastname}"

print(type(full_name("zakaria", "nabhan")))

#lambda get email

email_f = lambda firstname, lastname : "firstname, lastname"

print(email_f)

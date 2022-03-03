#Return the Remainder from Two Numbers

'''
There is a single operator in Python,
capable of providing the remainder of a division operation.
Two numbers are passed as parameters. The first parameter divided by
the second parameter will have a remainder,
possibly zero. Return that value.
'''

def remainder(num1, num2):
    """
    :param num1:
    :param num2:
    :return:
    """
    return num1 % num2

print(remainder(1, 3))
print(remainder(3, 4))
print(remainder(5, 5))
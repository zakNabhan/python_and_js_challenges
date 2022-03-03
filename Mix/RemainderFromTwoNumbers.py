'''
There is a single operator in Python, capable of providing the remainder
of a division operation.
Two numbers are passed as parameters. The first parameter divided
 by the second parameter will have a remainder, possibly zero. Return that value.
'''


def remainder(param1, param2):
    """
    :param param1:
    :param param2:
    :return:
    """
    result = param1 % param2
    return result


print(remainder(1, 3))
print(remainder(3, 4))
print(remainder(-9, 45))
print(remainder(5, 5))
print(remainder(7, 2))


# other version
remainder = lambda x, y: x % y
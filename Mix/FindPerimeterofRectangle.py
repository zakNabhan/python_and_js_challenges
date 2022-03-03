'''
Create a function that takes length and width and finds the
perimeter of a rectangle.


'''


def find_perimeter(length, width):
    """
    :param length:
    :param width:
    :return:
    """
    return 2 * (length + width)

print(find_perimeter(6, 7))
print(find_perimeter(20, 10))
print(find_perimeter(2, 9) )

# other version


def find_permeter(param1, param2):
    return  param1 * 2 + param2 * 2

#other version
find_perimeter=lambda a,b:2*(a+b)
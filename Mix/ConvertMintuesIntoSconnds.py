'''
Write a function that takes an integer minutes and converts it to seconds.
'''

def convert(mintues):
    """
    :param mintues:
    :return:
    """
    return mintues * 60

print(convert(5))
print(convert(3))
print(convert(2))


# convert hours and mintues into Scondes

def convert(hours, minutes):

    return hours*60*60 + minutes*60


print(convert(1, 3))

print(convert(2, 0))

print(convert(0, 0))

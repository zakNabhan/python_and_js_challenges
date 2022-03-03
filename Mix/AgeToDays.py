'''
Create a function that takes the age and return the age in days.

'''


def calc_age(age):
    """

    :param age:
    :return:
    """
    if age == 0 or age < 0:
        return 0
    else:
        return age * 365


print(calc_age(65))
print(calc_age(0))
print(calc_age(20))

# other version
calc_age = lambda n: n * 365

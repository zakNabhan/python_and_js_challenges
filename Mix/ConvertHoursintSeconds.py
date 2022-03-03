"""

Write a function that converts hours into seconds.
Write a function that converts hours into seconds.

"""


def convert_hours_into_sconds(hours):
    """
    :param hours:
    :return: how many sconds in hours
    """
    if hours > 0:
        return hours * 60 * 60


'''
other version
'''


def how_many_seconds(hours):
    seconds = hours * 3600
    return seconds


print(convert_hours_into_sconds(2))
print(convert_hours_into_sconds(10))
print(convert_hours_into_sconds(24))

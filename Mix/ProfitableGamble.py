'''
Create a function that takes
three arguments prob, prize, pay and returns True if prob * prize > pay;
otherwise return False.
'''


def profitable_gamble(prob, prize, pay):
    """
    :param prob:
    :param prize:
    :param pay:
    :return:
    """
    if prob * prize > pay:
        return True
    else:
        return False

print(profitable_gamble(0.2, 50, 9))
print(profitable_gamble(0.9, 1, 2))
print(profitable_gamble(0.9, 3, 2))
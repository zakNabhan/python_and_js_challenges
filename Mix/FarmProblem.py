'''
In this challenge, a farmer is asking you to tell
him how many legs can be counted among all his animals.
 The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal
for each species.
You have to implement a function that returns the total
number of legs of all the animals.
'''


# other version
animals = lambda c, m, p: c * 2 + m * 4 + p * 4

def animals(chickens, cows, pigs):
    """
    :param chickens:
    :param cows:
    :param pigs:
    :return:
    """
    total = chickens * 2 + cows * 4 + pigs * 4
    return total


print(animals(2, 3, 5))
print(animals(1, 2, 3))
print(animals(5, 2, 8))

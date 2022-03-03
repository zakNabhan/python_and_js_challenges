'''
Create a function that finds the maximum range of a triangle's third edge,
where the side lengths are all integers.

(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.
Don't forget to return the result.

'''


def next_edge(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    if x and y > 0:
        ergebnis = (x + y) - 1
        return ergebnis


print(next_edge(8, 10))
print(next_edge(5, 7))
print(next_edge(9, 2))

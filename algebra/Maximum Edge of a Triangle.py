#Maximum Edge of a Triangle

'''
Create a function that finds the maximum
 range of a triangle's third edge, where the side lengths are all integers.

Notes
(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.
Don't forget to return the result.
'''

def next_edge(side1, side2):
    """

    :param side1:
    :param side2:
    :return:
    """
    return (side1 + side2) - 1

print(next_edge(8, 10))
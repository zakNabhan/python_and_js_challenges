""" 
Geometry 1: Length of Line Segment

Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.
Examples

line_length([15, 7], [22, 11]) ➞ 8.06

line_length([0, 0], [0, 0]) ➞ 0

line_length([0, 0], [1, 1]) ➞ 1.41

Notes

    The order of the given numbers is X, Y.
    This challenge is easier than it looks.
    Round your result to two decimal places.
"""


import math
def line_length(dot1, dot2):
    return math.hypot(dot1, dot2)

if __name__ =="__main__":
    print(line_length([15, 7],[22,11]))
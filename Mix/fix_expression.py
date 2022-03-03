""" 
Fix the Expression

Fix the code in the Code tab so the function returns true if and only if x is equal to 7. Try to debug code and pass all the tests.
Examples

is_seven(4) ➞ False

is_seven(9) ➞ False

is_seven(7) ➞ True

Notes

The bug can be hard to find, so look closely!

"""


def is_seven(num):
    state = False
    if num is 7:
        state = True
    return state


if __name__ == "__main__":
    print(is_seven(4))
    print(is_seven(9))
    print(is_seven(7))

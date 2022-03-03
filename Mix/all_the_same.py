""" 
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

Example:
all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True

"""


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if len(elements) == 0:
        return True
    else:
        result =  elements.count(elements[0]) == len(elements)
        return result
    
   


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    print(all_the_same([]))
    # These "asserts" are used for self-checking and not for an auto-testing
 
    print("Coding complete? Click 'Check' to earn cool rewards!")

'''
Filter Strings from Array
Create a function that takes a list of strings and integers,
and filters out the list so that it returns a list of integers only.
'''


def filter_list(lst):
    new_lst_int = []
    new_lst_str = []

    for x in lst:
        if type(x) == int:
            new_lst_int.append(x)
        else:
            type(x) == str
            new_lst_str.append(x)
    return new_lst_str

print(filter_list([1, 2, 3, "a", "b", 4]))
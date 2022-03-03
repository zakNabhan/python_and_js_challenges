'''
Create a function to concatenate two integer lists.

'''



def concat(list_1 =[], list_2 =[]):
    """
    :param list_1:
    :param list_2:
    :return:
    """
    liste = list_1 + list_2
    return liste

print(concat([1, 3, 5], [2, 6, 8]))


# Another way to join two lists


def concat(list_1 =[], list_2 =[]):
    """
    :param list_1:
    :param list_2:
    :return:
    """

    for x in list_2:
        list_1.append(x)
    return list_1

print(concat([1, 3, 5], [2, 6, 8]))


# other version
'''

def concat(lst1, lst2):
	lst1.extend(lst2)
	return lst1
	
	def concat(lst1, lst2):
	return lst1 + lst2
	
'''
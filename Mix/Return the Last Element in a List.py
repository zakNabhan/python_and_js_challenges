'''
Create a function that accepts a
list and returns the last item in the list.
The list can be either homogeneous or heterogeneous.
'''



def get_last_item(lst=[]):
    if lst is None:
        return "Leere List"
    else:
        return lst.pop()


print(get_last_item([1, 2, 3]))
print(get_last_item(["cat", "dog", "duck"]))
print(get_last_item([True, False, True]))
print(get_last_item([]))

#other version
def get_last_item(lst):
	 return lst.pop()
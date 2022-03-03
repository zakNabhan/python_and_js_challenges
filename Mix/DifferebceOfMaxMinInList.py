'''
Create a function that takes a list and returns
the difference between the biggest and smallest numbers

'''


def difference_max_min(lst):

    max_number = lst[0]
    min_number = lst[0]

    for i in lst:
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i
    difference = max_number - min_number
    return "Differenc: "+ str(difference) + " Maxnumber:" + str(max_number) + \
           " Minnumber: " + str(min_number)

print(difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]))



# other task


def difference(nums):
    """

    :param nums:
    :return: differnnce between two maximum numbers
    """

    max_num = nums[0]
    min_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
        if x < min_num:
            min_num = x
    return max_num - min_num


print(difference([10, 15, 20, 2, 10, 6]))
print(difference([-3, 4, -9, -1, -2, 15]))
print(difference([4, 17, 12, 2, 10, 2]))

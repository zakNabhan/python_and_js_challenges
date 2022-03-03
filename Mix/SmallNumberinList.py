'''
Create a function that takes
a list of numbers and returns the smallest number in the list.

'''


def find_smallest_num(nums):
    """

    :param nums:
    :return:
    """

    '''
    find max
      largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest
    '''
    smallnums = nums[0]
    for i in nums:
        if i < smallnums:
            smallnums = i
    return smallnums


print(find_smallest_num([34, 15, 88, 2]))

# Maximum Difference
'''
Given a list of integers, 
return the difference between the 
largest and smallest integers in the list.


'''
print("_________________________________")


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

# other version

def difference(nums):
    return max(nums) - min(nums)

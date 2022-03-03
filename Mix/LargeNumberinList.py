'''
Create a function that takes a list of numbers.
Return the largest number in the list.
'''


def findLargestNum(nums=[]):
    """
    :param nums:
    :return:
    """
    return max(nums)


print(findLargestNum([4, 5, 1, 3]))
print(findLargestNum([300, 200, 600, 150]))
print(findLargestNum([1000, 1001, 857, 1]))


# other version

def findLargestNum(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest

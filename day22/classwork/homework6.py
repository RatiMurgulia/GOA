# Find Maximum and Minimum Values of a List
# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language )
# that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
# Examples (Input -> Output)
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
def minimum(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num
    
def maximum(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
# test.assert_equals(minimum([-52, 56, 30, 29, -54, 0, -110]), -110)
# test.assert_equals(minimum([42, 54, 65, 87, 0]), 0)
# test.assert_equals(minimum([1, 2, 3, 4, 5, 10]), 1)
# test.assert_equals(minimum([-1, -2, -3, -4, -5, -10]), -10)

# 2 way
def minimum(arr):
    arr.sort()
    min_num = min(arr)
    return min_num
    
def maximum(arr):
    arr.sort()
    max_num = max(arr)
    return max_num
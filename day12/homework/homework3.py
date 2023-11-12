# Given an array of integers your solution should find the smallest integer

# 1 way
def find_smallest_int(arr):
    new_arr = min(arr)
    return new_arr
# 2 way
def find_smallest_int(arr):
    arr.sort()
    return arr[0]
# 3 way
def find_smallest_int(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num
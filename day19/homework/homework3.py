# Sum Arrays
# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer.
# If the array does not contain any numbers then you should return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

def sum_array(a):
    my_sum = 0
    for i in a:
        my_sum += i
    return my_sum
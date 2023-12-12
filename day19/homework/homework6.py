# Calculate average
# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.
def find_average(numbers):
    average = 0
    for i in numbers:
        average += i / (len(numbers))
    return average
# test.assert_equals(find_average([1, 2, 3]), 2, "Failed for [1, 2, 3]")
# test.assert_equals(find_average([]), 0, "Failed for []")
# test.assert_approx_equals(find_average([1, 2]), 1.5, margin=1e-3, message="Failed for [1, 2]")
        
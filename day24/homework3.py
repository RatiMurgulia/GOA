# Is n divisible by x and y?
# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    return False
# test.assert_equals(is_divisible(3,2,2),False)
# test.assert_equals(is_divisible(3,3,4),False)
# test.assert_equals(is_divisible(12,3,4),True)
# test.assert_equals(is_divisible(8,3,4),False)
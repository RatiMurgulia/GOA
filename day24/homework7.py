# If you can't sleep, just count sheep!!
# If you can't sleep, just count sheep!!
# Given a non-negative integer, 3 for example
# return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
def count_sheep(n):
    result = ""
    if n == 0:
        return ""
    for i in range(1,n + 1):
        result += str(i) + " sheep..."
    return result
# test.assert_equals(count_sheep(0), "");
# test.assert_equals(count_sheep(1), "1 sheep...");
# test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
# test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")


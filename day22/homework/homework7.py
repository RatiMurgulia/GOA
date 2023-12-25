# You only need one - Beginner
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not
def check(seq, elem):
    for element in seq:
        if element == elem:
            return True
    return False
# (False, ([78, 117, 110, 99, 104, 117, 107, 115], 8)),
# (True, ([101, 45, 75, 105, 99, 107], 107)),
# (True, ([80, 117, 115, 104, 45, 85, 112, 115], 45)),
# (True, (['t', 'e', 's', 't'], 'e')),

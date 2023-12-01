# Invert values
# Given a set of numbers, return the additive inverse of each
# Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    my_arr = []
    for i in lst:
        if i > 0:
            my_arr.append(i * -1)
        if i < 0:
            my_arr.append(i * -1)
    return my_arr

# correct way
def invert(lst):
    my_arr = []
    if len(lst) == 0:
        return []
    for i in lst:
        my_arr.append( i * -1)
    return my_arr

    

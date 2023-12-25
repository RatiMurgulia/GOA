# Beginner - Reduce but Grow
def grow(arr):
    result = []
    sum = 1
    for element in arr:
        sum *= element
    # result.append(sum)
    return sum


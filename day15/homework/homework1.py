# Square(n) Sum
def square_sum(numbers):
    my_sum = 0
    for num in numbers:
        my_sum += (num ** 2)
    return my_sum
# Convert number to reversed array of digits
def digitize(n):
    my_arr = []
    for i in str(n):
        my_arr.append(int(i))
    return my_arr[::-1]
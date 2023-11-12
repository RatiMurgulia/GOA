# Write a function that accepts an integer n and a string s as parameters
# and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return(repeat * string)

# 2 way
def repeat_str(repeat, string):
    my_str = ""
    for i in range(repeat):
        my_str += string
    return my_str


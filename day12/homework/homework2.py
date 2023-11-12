# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters

# 1 way
def remove_char(s):
    return (s[1:-1])

# 2 way code not working!
def remove_char(s):
    my_str = ""
    for i in s:
        if i != s[0] and i != s[-1]:
            my_str += i 
    return my_str
# test.assert_equals(remove_char('eloquent'), 'loquen')
# test.assert_equals(remove_char('country'), 'ountr')
# test.assert_equals(remove_char('person'), 'erso')
# test.assert_equals(remove_char('place'), 'lac')
# test.assert_equals(remove_char('ok'), '')
# test.assert_equals(remove_char('ooopsss'), 'oopss')
    


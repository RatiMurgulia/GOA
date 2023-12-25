# Jenny's secret message
# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.

def greet(name):
    if name != "Johnny":
        return "Hello, {}!".format(name)
    return "Hello, my love!"
# test.assert_equals(greet("James"), "Hello, James!")
# test.assert_equals(greet("Jane"), "Hello, Jane!")
# test.assert_equals(greet("Jim"), "Hello, Jim!")
# test.assert_equals(greet("Johnny"), "Hello, my love!")
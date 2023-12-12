# Fake Binary
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.
# Note: input will never be an empty string
def fake_bin(x):
    my_str = ""
    for i in x:
        if int(i) < 5:
            my_str += "0"
        elif int(i) >= 5:
            my_str += "1"
    return my_str

# 2 way
def fake_bin(x):
    my_str = ""
    for a in x:
        for b in a:
            if int(b) < 5:
                my_str += "0"
            if int(b) >= 5:
                my_str += "1"
    return my_str
                
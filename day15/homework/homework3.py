# Remove String Spaces
def no_space(x):
    new_str = ""
    for i in x:
        if i != " ":
            new_str += i
    return new_str
print(no_space("nika keshelava is the CEO of GOA"))
# test.assert_equals(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
# test.assert_equals(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
# test.assert_equals(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
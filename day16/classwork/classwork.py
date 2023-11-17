# Identity Operators:
x = [1, 2, 3]
y = x

is_same_object = x is y
print(is_same_object)
# დაიპრინტება True რადგან x არის იგივე y
x = [1, 2, 3]
y = x

is_same_object = x is not y
print(is_same_object)
# დაიპრინტება False




# Arithmetic Operators:
x = 10
y = 3

addition_result = x + y  # 10 + 3 = 13
subtraction_result = x - y  # 10 - 3 = 7
multiplication_result = x * y  # 10 * 3 = 30
division_result = x / y  # 10 / 3 = 3.333...
integer_division_result = x // y  # 10 // 3 = 3
modulus_result = x % y  # 10 % 3 = 1
exponentiation_result = x ** y  # 10 ** 3 = 1000

# Comparison Operators:
a = 5
b = 7

is_equal = a == b  # False
not_equal = a != b  # True
greater_than = a > b  # False
less_than = a < b  # True
greater_than_or_equal = a >= b  # False
less_than_or_equal = a <= b  # True

# Logical Operators:
p = True
q = False

logical_and = p and q  # False
logical_or = p or q  # True
logical_not_p = not p  # False

# Assignment Operators:
x = 10

x += 5  # x is now 15
x -= 3  # x is now 12
x *= 2  # x is now 24
x /= 4  # x is now 6.0
x //= 2  # x is now 3.0 
x %= 2  # x is now 1.0
x **= 3  # x is now 1.0 (raised to the power of 3)

# Membership Operators:
fruits = ['apple', 'banana', 'cherry']

is_in_list = 'banana' in fruits  # True
is_not_in_list = 'orange' not in fruits  # True

# Identity Operators:
x = [1, 2, 3]
y = x

is_same_object = x is y  # True
is_not_same_object = x is not None  # True

# Other Operators:
text = "Hello, world!"
slice_result = text[0:5]  # "Hello"

# Integer (int):
x = 5
y = -10
# Floating-point (float):
pi = 3.14159
price = 19.99
# String (str):
name = "Alice"
message = 'Hello, world!'
# Boolean (bool):
is_true = True
is_false = False
# List (list):
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']

# Reversed String
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string): # მაგ. "hello"-ი ში არის 5 ინდექსზე მდგომი ელემენტი 01234
    new_str = ""
    i = len(string) # i = 5 len()-ით დათვლა იწყება 1-დან
    while i > 0:  # 5 > 0:
        new_str += string[i-1] # (5 - 1 = 4)  (i = 4)
    return new_str

# 2 way
def solution(string):
    my_str = string[::-1]
    return my_str

# 3 way
def solution(string):
    my_str = ""
    for i in range(len(string)):
        my_str += string[-i -1]
        i -= 1
    return my_str

# Sum of positive
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
def positive_sum(arr):
    sum = 0
    for element in arr:
        if element > 0:
            sum += element
    return sum
# test.assert_equals(positive_sum([1,2,3,4,5]),15)
# test.assert_equals(positive_sum([1,-2,3,4,5]),13)
# test.assert_equals(positive_sum([-1,2,3,4,-5]),9)



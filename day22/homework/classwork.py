# Count the Monkeys!
def monkey_count(n):
    arr = []
    for i in range(1,n+1): # დაიწყოს 1-დან n სიის სიგრძეს დამატებული 1,რადგან გადმოცემულ სიას სრულად გადავუაროთ
        arr.append(i)
    return arr
# test.assert_equals(monkey_count(5), [1, 2, 3, 4, 5])
# test.assert_equals(monkey_count(3), [1, 2, 3])
 # test.assert_equals(monkey_count(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
# test.assert_equals(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Find the first non-consecutive number
# for example
# arr = [1, 2, 4, 5, 6]
def first_non_consecutive(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] -1: # arr-სიიდან i ინდექსზე ანუ 0 ინდექსზე მყოფი ელემენტი თუ გაუტოლდება
# arr-სიიდან i ანუ 0 ინდექსზე მყოფ ელემენტს +1 ანუ შემდეგ ინდექსზე მყოფ ელემენტს და ამ შემდეგ ინდექსზე მყოფ ელემენტს -1
            continue # ნიშნავს გაგრძელებას
        return arr[i + 1]
    return None
# test.assert_equals(first_non_consecutive([1,2,3,4,6,7,8]), 6)
# test.assert_equals(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
# test.assert_equals(first_non_consecutive([4,6,7,8,9,11]), 6)
# test.assert_equals(first_non_consecutive([4,5,6,7,8,9,11]), 11)


# Removing Elements
# Take an array and remove every second element from the array.
# Always keep the first element and start removing with the next element.
def remove_every_other(my_list):
    arr = []
    for i in range(len(my_list)):
        if i % 2 == 0: # თუ სიაში i ინდექსი % 2 == 0:
            arr.append(my_list[i]) # my_list სიიდან i-ზე მდგომი ინდექსი
    return arr

# test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
#                    ['Hello', 'Hello Again'])
# test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
#                    [1, 3, 5, 7, 9])
# test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
# test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
#                    [['Goodbye']])


# Reversed Words

# Complete the solution so that it reverses all of the words within the string passed in.
# Words are separated by exactly one space and there are no leading or trailing spaces.
# Example(Input --> Output):
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
def reverse_words(s):
    x = s.split()
    x.reverse()
    final_str = ""
    for element in x:
        final_str += element + " " # + " " ნიშნავს რომ string-ის ელემენტს მივუმატეთ space-ი
    return final_str[:-1] # :-1 დავწერეთ იმიტომ რომ string-ის ელემენტს როცა მივუმატეთ space-ი ბოლოშიც მიემატა
# და ამიტომ ბოლო space-ი წავშალეთ რადგან ამოცანაში არ გვჭირდებოდა
# test.assert_equals(reverse_words("hello world!"), "world! hello"

# 2 way
    return " ".join(s.split()[::-1])



# Total amount of points

# Our team's match results are recorded in a collection of strings.
# Each match is represented by a string in the format "x:y"
# where x is our team's score and y is our opponents score.
# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
def points(games):
    score = 0
    for element in games: # for ციკლი სიაში
        split_arr = element.split(":") # split(":") ის საშუალებით სიაში ელემენტი გავხლიჩეთ :-ში
        if split_arr[0] > split_arr[1]: # გასპლიტული სიის პირველი ელემენტი შევადარეთ მეორე ელემენტს
            score += 3
        elif split_arr[0] == split_arr[1]:
            score += 1
    return score
# test.assert_equals(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30)
# test.assert_equals(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10)
# test.assert_equals(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0)
# test.assert_equals(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15)




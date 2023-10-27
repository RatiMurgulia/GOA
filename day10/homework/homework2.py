# შექმენით random password generator პროგრამა რომელშიც დაგენერირდება პაროლი 8 სიმბოლოიანი
# სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#
# 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე
# 4 სიმბოლო იქნება ციფრები 215346347347


import random

string = input("Enter a string: ")
symbol = input("Enter a symbol: ")
number = input("Enter a number: ")


string = random.choice(string) + random.choice(string)
symbol = random.choice(symbol) + random.choice(symbol)
number = random.choice(number) + random.choice(number) + random.choice(number) + random.choice(number)

complete_password = string + symbol + number
print("Your new password is: " + complete_password)

# 2 way
arr_of_strings = []
for i in range(5):
    text = input("Enter a text: ")
    arr_of_strings.append(text)
for j in range(2):
    final_str = arr_of_strings[random.randint(0,2)]

arr_of_symbols = []
for x in range(5):
    symbol = input("Enter a symbol: ")
    arr_of_symbols.append(symbol)
for y in range(2):
    final_symbol = arr_of_symbols[random.randint(0,2)] 

arr_of_numbers = []
for a in range(5):
    number = input("Enter a number: ")
    arr_of_numbers.append(number)
for b in range(2):
    final_number = arr_of_numbers[random.randint(0,2)]

print("Your new password is: " + final_str + final_symbol + final_number)
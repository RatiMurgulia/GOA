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

# 2 Professional way
import random

password = "" # ცარიელი სტრინგი
chars = "qwertyuiopasdfghjklzxcvbnm"
symbols = "!@#$%^&*()"
numbers = "0123456789"

for i in range(4): # ციკლი დატრიალდება 4-ჯერ 0-დან 3-მდე და აირჩევს სიმბოლოს 4-ჯერ
    password += random.choice(numbers) # password-ის ცარიელი string-ი გაიზრდება numbers-იდან random არჩეული ელემენტებით 4-ჯერ 0-დან 3-მდე

for i in range(2): # ციკლი დატრიალდება 2-ჯერ 0-დან 1-მდე და აირჩევს სიმბოლოს 2-ჯერ
    password += random.choice(chars) # password-ის ცარიელი string-ი გაიზრდება chars-იდან random არჩეული ელემენტებით 2-ჯერ 0-დან 1-მდე
    password += random.choice(symbols) # password-ის ცარიელი string-ი გაიზრდება symbols-იდან random არჩეული ელემენტებით 2-ჯერ 0-დან 1-მდე

print(password)

# 3 Professional way
# შევქმნათ საბოლოო პაროლის სია
# დავწეროთ კოდიისე რომ საბოლოო პაროლის სიმბოლოები იყოს არეული და არ მეორდებოდეს ერთი სიმბოლო ორჯერ
# მაგრამ ეს კოდი სიმბოლოებს მაინც გაიმეორებს
import random

my_arr = []

chars = "qwertyuiopasdfghjklzxcvbnm"
symbols = "!@#$%^&*()"
numbers  = "0123456789"

for i in range(4):
    my_arr.append(random.choice(numbers)) # my_arr[] ცარიელ სიაში ჩავარდება random არჩეული 4 ელემენტი numbers-იდან

for i in range(2):
    my_arr.append(random.choice(chars)) # my_arr[] ცარიელ სიაში ჩავარდება random არჩეული 2 ელემენტი chars-იდან
    my_arr.append(random.choice(symbols)) # my_arr[] ცარიელ სიაში ჩავარდება random არჩეული 2 ელემენტი symbols-იდან

final_password = "" # ცარიელი სტრინგი
for i in range(len(my_arr)): # for ციკლი len(my_arr)-ს სიგრძემდე
    current_char = random.choice(my_arr) # ახალ ცვლადს current-ს მიენიჭა მნიშვნელობა მაგ. my_arr["1", "^", "u", 9", "3", "m", "#", "0"] სიიდან random არჩეული ელემენტების მნიშვნელობა
# random.choice(my_arr) იმიტომ დავწერეთ რომ ახალ ცვლადში current_char-ში არეულად ჩავარდეს ეს ელემენტები
    final_password += current_char # საბოლოო ცვლადი final_password-ი გავზარდეთ current_char-ის არეული ელემენტებით
    my_arr.remove(current_char) # რათა my_arr[] სიაში არსებული ყველა სიმბოლო ერთხელ გამოვიყენოთ

print(final_password)


# შექმენით random password generator პროგრამა რომელშიც დაგენერირდება პაროლი 40 სიმბოლოიანი
# სადაც აუცილებლად 6 სიმბოლო იქნება !@#$%^&*()
# 25 სიმბოლო იქნება qwertyuiopasdfghjklzxcvbnm
# 9 სიმბოლო იქნება 1234567890
import random

my_arr = []

chars = list("qwertyuiopasdfghjklzxcvbnm")
symbols = list("!@#$%^&*()")
numbers = list("1234567890")

for i in range(9):
    random_num = random.choice(numbers)
    my_arr.append(random_num)
    numbers.remove(random_num)

for i in range(25):
    random_char = random.choice(chars)
    my_arr.append(random_char)
    chars.remove(random_char)

for i in range(6):
    random_symbol = random.choice(symbols)
    my_arr.append(random_symbol)
    symbols.remove(random_symbol)

final_password = ""
for i in range(len(my_arr)):
    current_char = random.choice(my_arr)
    final_password += current_char
    my_arr.remove(current_char)

print("The password is:" ,final_password)
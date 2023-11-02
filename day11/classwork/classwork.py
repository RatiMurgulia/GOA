name = "rati"
print(name.upper())
# დაიპრინტება RATI დიდი სიმბოლოებით upper() ფუნქციის გამოყენებით

print("mari".upper())
# დაიპრინტება MARI დიდი სიმბოლოებით

car = "SUBARU"
print(car.lower())
# დაიპრინტება subaru პატარა სიმბოლოებით lowe() ფუნქციის გამოყენებით

print("FORD".lower())
# დაიპრინტება ford პატარა სიმბოლოებით

city = "london"
print(city.capitalize())
# დაიპრინტება London პირველი დიდი სიმბოლოთი capitalize() ფუნქციის გამოყენებით

print("football".capitalize())
# დაიპრინტება Football

item = "smartwatch"
item2 = item.upper()
print(item2)
# დაიპრინტება SMARTWATCH დიდი სიმბოლოებით

sport = "football"
print(sport.find("o"))
# დაიპრინტება 1 რადგან find() ფუნქციაში გადაცემული ("o") იდგა 1 ინდექსზე sport-ში
# find() ფუნქცია აბრუნებს გადაცემული სიმბოლოს ინდექს მხოლოდ ერთხელ
# თუ ერთნაერი სიმბოლოები ბევრია სტრიქონში find() ფუნქცია იპოვის ყველაზე ახლო ინდექსს

print("germany".find("r"))
# დაიპრინტება 2 რადგან "r" დგას 2 ინდექსზე

print("robot".find("v"))
# დაიპრინტება -1 თუ მნიშვნელობა ვერ მოიძებნა სტრიქონში

movies = ["Avatar", "Titanic", "Avengers"]
print(len(movies))
# დაიპრინტება 3 len() ფუნქციის გამოყენებით ვიპოვეთ movie სიის ელემენტების რაოდენობა
# len() ფუნქცია ითვლის 1-დან

print(len("rati"))
# დაიპრინტება 4

songs = ["Yesterday", "Hello", "Believer"]
songs.append("Imagine")
print(songs)
# დაიპრინტება ['Yesterday', 'Hello', 'Believer', 'Imagine'] ბოლოში დაემატა Imagine
# append() ფუნქცია სიაში ამატებს ყოველთვის ბოლოში

name = ["rati", "nika", "mari"]
name2 = [] # ცარიელი სია
name2.append("rati") # # ცარიელ name2 სიაში დაემატება "rati"
print(name2)
# დაიპრინტება ['rati']

name = ["rati", "nika", "mari"]
name2 = [] # ცარიელი სია
name2.append(name[1]) # name2-სიაში append()-ით ვამატებთ name-სიის [1] ელემენტზე მდგომ მნიშვნელობას "nika"-ს
print(name2)
# დაიპრინტება ['nika']
# append() ფუნქცია არის სიებისთვის
# append() ფუნციით ვერ გამოიყენებთ სტრიქონზე

items = ["book", "pen", "pencil"]
items.insert(2,"marker")
print(items)
# დაიპრინტება ['book', 'pen', 'marker', 'pencil']
# insert() ფუნქცია არის ჩასმა
# 2 არის item-სიის ინდექსი რომელიც არის "pencil" insert() ფუნქციით ჩავსვით "maker"-ი item-სიის 2 ელემენტამდე ანუ "pencil"-მდე
# insert() ფუნქცია იღებს 2 არგუმენტს: 1)რომელ ინდექსზე ჩავსვათ 2)რა ჩავსვათ

lessons = ["Maths","English","Physics"]
lessons.pop(1)
print(lessons)
# დაიპრინტება ['Maths', 'Physics']
# pop() ფუნქციის გამოყენებით გადავახტით lesson-სიაში pop(1) ანუ [1] ინდექსზე მყოფ ელემენტს "English"-ს

fruits = ["apple", "banana", "cherry"]
x = fruits.index("cherry")
print(x)
# დაიპრინტება 2 რადგან "cherry" fruit ცვლადში დგას 2 ინდექსზე

students = ["giorgi", "rati", "salome", "anri", "demetre"]
grades = [10, 20, 30, 40, 50]
giorgis_index = students.index("giorgi") # ვიპივეთ "giorgi"-ს index-ი student სიაში რომელიც არის 0 index-ზე
giorgis_grade = grades[giorgis_index] # giorgis_grade ცვლადს მივანიჭეთ მნიშვნელობა grade[]-სია რომელშიც გადავეცით giorgis_index-ი რომელიც დგას 0 index-ზე
print(giorgis_grade + 10)
# დაიპრინტება 20


# def ფუნქცია

def bichebtan_misalmeba(): 
    print("hello Gio")
    print("hello Nika")
    print("hello Tornike")
    print("hello Luka")
bichebtan_misalmeba()

# დაიპრინტება
# hello gio
# hello nika
# hello tornike
# hello Luka

def bichebtan_misalmeba(): 
    print("hello Gio")
    print("hello Nika")
    print("hello Tornike")
    print("hello Luka")
print("dila")
bichebtan_misalmeba()
print("shuadge")
bichebtan_misalmeba()
print("sagamo")
bichebtan_misalmeba()

# დაიპრინტება
# dila
# hello Gio    
# hello Nika   
# hello Tornike
# hello Luka   
# shuadge      
# hello Gio    
# hello Nika   
# hello Tornike
# hello Luka   
# sagamo
# hello Gio
# hello Nika
# hello Tornike
# hello Luka

def misalmeba(name): # (saxeli) არის პარამეტრი რომელიც არის ზოგადი სახელი
    print("mogesalmebi " + name)
misalmeba("Nika") # misalmeba() არის ფუნქციის გამოძახება რომელსაც გადაეცემა არგუმენტად ნებისმიერი სახელი მაგ. "Nika"
misalmeba("Rati")
misalmeba("Gabriel")
misalmeba("Sandro")

# დაიპრინტება
# mogesalmebi Nika
# mogesalmebi Rati
# mogesalmebi Gabriel
# mogesalmebi Sandro

def misalmeba(name, age): # გადავეცით 2 არგუმენტი name და age
    print("mogesalmebi " + name)
    print("sheni asakia " , age) # , გამოყენებით ავტომატურად შეერთდება string-ი და integer-ი და არ დაგვჭირდება integer-ის string-ად გარდაქმნა

misalmeba("Nika", 15)
misalmeba("Rati" , 27)

# დაიპრინტება
# mogesalmebi Rati
# sheni asakia  27

def your_name():
    name = input("Enter your name: ") # name ცვლადში მნიშვნელობის შეყვანა input()-ით მაგ. Rati-ს
    print("Your name is " + name) # დაიპრინტება Your name is + name ანუ input-ით შეყვანილი სახელი Rati
your_name() # ვაბრუნებთ პარამეტრს

numbers = list(range(10)) # numbers ცვლადი რომელსაც მნიშვნელობა მივანიჭეთ range(10) 0-დან 9-მდე ჯამში 10 რიცხვი,list-ის საშუალებით გადავაქციეთ სიად
print(numbers)
# დაიპრინტება  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(range(3, 8)) # range()-ს გადავეცით 2 არგუმენტი #start #finish
print(numbers)
# დაიპრინტება [3, 4, 5, 6, 7]

numbers = list(range(5, 20, 2)) # range()-ს გადავეცით 3 არგუმენტი #start #finish #step
print(numbers)
# დაიპრინტება [5, 7, 9, 11, 13, 15, 17, 19] 5-დან 19-მდე ყოველი 2-ე

x = list(range(7, 3, -1)) # -1 ნიშნავს ბოლო ელემენტიდან დაწყებას
print(x)
# დაიპრინტება [7, 6, 5, 4] 7-დან 4-მდე -1 ის გამოყენებით სია დაიპრინტა მაღლიდან ქვემოთ

y = list(range(7, 3, -2))
print(y)
# დაიპრინტება [7, 5] 7-დან 3-მდე ყოველი 2-ე

# slicing დაჭრა
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) # 2-დან 6-მდე
print(squares[3:8]) # 3-დან 8-მდე
print(squares[0:1]) # 0-დან 1-მდე
# დაიპრინტება
# [4, 9, 16, 25]
# [9, 16, 25, 36, 49]
# [0]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[0:7]) # 0-დან 7-მდე
# დაიპრინტება [0, 1, 4, 9, 16, 25, 36]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:]) # 7-დან ბოლომდე
# დაიპრინტება [49, 64, 81]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2]) # :: დასაწყისიდან ბოლომდე ყოველი 2-ე რიცხვი
# დაიპრინტება [0, 4, 16, 36, 64]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:8:3]) # 2-დან 8-მდე ყოველი 2-ე რიცხვი
# დაიპრინტება [4, 25]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1::4]) # 1-დან ბოლომდე ყოველი 4-ე რიცხვი
# დაიპრინტება [1, 25, 81]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1]) # 1-დან -1 მდე -1 არის ნეგატიური index-ი -1 იქნება 81 და დაიპრინტება 1-დან 81-მდე
# დაიპრინტება [1, 4, 9, 16, 25, 36, 49, 64]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:5:-1]) 
# დაიპრინტება [49, 36]

squares = [5, 4, 3, 2, 1]
print(squares[::-1]) # ::-1 არის სიის შეტრიალება
# დაიპრინტება [1, 2, 3, 4, 5]

squares = [5, 4, 3, 2, 1]
print(squares[1:-1]) # :1-დან -1 მდე ბოლო რიცხვამდე ანუ 1-მდე
# დაიპრინტება [4, 3, 2]


import random

print(random.randint(1,100)) # 1-დან 100-მდე
# დაიპრინტება random რიცხვი 1-დან 100-მდე

my_students = ["nika", "gabrieli", "dato", "luka", "sandro"]
print(my_students[random.randint(0,4)])
# დაიპრინტება my_student სიაში random ელემენტი 0-დან 4-მდე

import random
my_students = ["nika", "gabrieli", "dato", "luka", "sandro"]
print(random.choice(my_students))
# არჩევს random ელემენტს my_students სიაში

import random
my_students = ["nika", "gabrieli", "dato", "luka", "sandro"]
for i in range(10):
    print(random.choice(my_students))
# დაიპრინტება 10 random არჩეული ელემენტი my_student სიაში

import random
my_students = ["nika", "gabrieli", "dato", "luka", "sandro"]
arr_of_cars = ["bmw", "mercedes", "prius", "subaru", "porsche", "mclaren"]

for i in range(len(my_students)):
    print(random.choice(my_students) + " won the car: " + random.choice(arr_of_cars))
# დაიპრინტება my_student-ის random არჩეული ელემენტი და დაემატება arr_of-cars-ის random არჩეული ელემენტი
# ასევე შეიძლება ერთი random ელემენტი განმეორდეს ბევრჯერ
# ასე რომ არ მოხდეს უნდა გადავაკეთოთ კოდი
import random
my_students = ["nika", "gabrieli", "dato", "luka", "sandro"]
arr_of_cars = ["bmw", "mercedes", "prius", "subaru", "porsche", "mclaren"]

for i in range(len(my_students)):
    winner = (random.choice(my_students)) # შევქმენით winner ცვლადი და მნიშვნელობად მივანიჭეთ my_student-ის random ელემენტი
    lucky_car = random.choice(arr_of_cars) # შევქმენით lucky_car ცვლადი და მნიშვნელობად მივანიჭეთ arr_of_car-ის random ელემენტი
    print(winner + " won the car: " + lucky_car)
    my_students.remove(winner) # my_student სიიდან თითოეულ იტერაციაზე წაიშალოს winner-ი რომ მეორედ არ განმეორდეს
    arr_of_cars.remove(lucky_car) # arr_of_car სიიდან თითოეულ იტერაციაზე წაიშალოს lucky_car-ი რომ მეორედ არ განმეორდეს
# დაწერილი კოდი მხოლოდ ერთხელ აირჩევს random ელემენტს

arr_of_cars = ["bmw", "mercedes", "prius", "subaru", "porsche", "mclaren"]
arr_of_cars.remove("bmw")
print(arr_of_cars)
# სიიდან წაიშლება "bmw" და დაიპრინტება სია



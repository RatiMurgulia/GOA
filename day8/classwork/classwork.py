for i in range(10):
    print(i)
# დატრიალდება for ციკლი და დაიპრინტება რიცხვები 0-დან 9-ის ჩათვლით

for i in range(10,20):
    print(i)
# დატრიალდება for ციკლი და დაიპრინტება რიცხვები 10-დან 20-მდე

for i in range(1,10,2): # (start finish step)
    print(i)
# დატრიალდება for ციკლი და დაიპრინტება რიცხვები 1-დან 20-მდე ყოველი მე2-ე

name = "mari"
for i in range(len(name)):
    print(i)
# დატრიალდება for ციკლი და დაიპრინტება რიცხვები იმდენჯერ რა სიგრძისაც არის name ცვლადი

for i in "rati":
    print(i)
# დაიპრინტება rati თითოეულ იტერაციაზე ერთი სიმბოლო
# r
# a
# t
# i

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala"]
foods.append("pizza") # pizza დაემატა სიის ბოლოში
print(foods[4]) # დაიპრინტება სიის 4-ე ელემენტი ახლად ჩასმული pizza
foods.insert(2, "lobiani") # insert() არის ჩასმა რომელსაც გადაეცემა ორი პარამეტრი,mwvadi და xachapuri შორის ჩავსვით "lobiani"
print(foods)
# დაიპრინტება ['khinkali', 'mwvadi', 'lobiani', 'xachapuri', 'xizilala', 'pizza']

i = 1
while i <= 12: # while ციკლი შესრულდება 1 დან 12 მდე
    print(i)
    i = i + 2 # i თითოეულ იტერაციაზე გაიზრდება 2-ით
print("Finished")
# დაიპრინტება
# 1
# 3
# 5
# 7
# 9
# 11
# რადგან თავდაპირველად i იყო 1 და შემდეგ i ყოველ ჯერზე გავზარდეთ 2-ით

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala"]
x_counter = 0
for food in foods:
    if food[0] == "x": # თუ foods სიაში თითოეული [0] ინდექსზე მდგომი ელემენტი გაუტოლდება "x"-ს
        x_counter += 1
print(x_counter)
# დაიპრინტება 2 რადგან [2] ინდექსზე დგას "xachapuri" და მის [0] ინდექსზე დგას x სიმბოლო

a = "nika 11 keshelava"
print(len(a))
# დაიპრინტება 17 რადგან len() ის დროს დათვლა იწყება 1-დან და ითვლება space-იც

# დავალება დაპრინტეთ 15
my_str = "nika 11 keshelava"
print(int(my_str[5]) + int(my_str[6] + "4"))

# მაგ: 13, 20, 7
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

my_sum = 0
if num1 % 2 == 1:
    my_sum += num1
if num2 % 2 == 1: 
    my_sum += num2
if num3 % 2 == 1:
    my_sum += num3
print("the sum of odd numbers is {}".format(my_sum))
# დაიპრინტება 20 რადგან შეიკრიბა მხოლოდ კენტი რიცხვებ 13 და 7
# format() ფუნქციის საშუალებით my_sum-ის ცვლადის ჩავსვით {} ფრჩხილებში


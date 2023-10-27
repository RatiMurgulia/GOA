a = 5
a += 10 # a გაიზარდოს 10-თ
print(a)
# დაიპრინტება 15

b = 13
c = 20 -7
print(b == c)
# დაიპრინტება True რადგან b-ს მნიშვნელობა გაუტოლდება c-ს

i = 1 # თავდაპირველად i არის 1-ის ტოლი
while i <= 12:
    print(i)
    i = i + 2 # 1-ის ტოლი i ყოველ ჯერზე გაიზრდება 2-ით 12-მდე
print("finished")
# დაიპრინტება
# 1   
# 3   
# 5   
# 7
# 9
# 11
# finished

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala"]
x_counter = 0
for food in foods:
    if food[0] == "x": # თუ food-ის თითოეული ელემენტის [0] ინდექსზე მყოფი სიმბოლო გაუტოლდება "x"-ს
        x_counter += 1 
print(x_counter)
# დაიპრინტება 2 რადგან food სიაში 2 ელემენტის [0] ინდექსზე დგას "x"

name = "rati"
print(name[1])
# დაიპრინტება a რადგან [1] ინდექსზე დგას a

my_list = ["nika", "rati", "gabrieli"]
for element in my_list: # თითოეული element-ი my_list სიიდან
    for char in element: # თითოეული სიმბოლო element-იდან
        print(char)
# დაიპრინტება
# n
# i
# k
# a
# r
# a
# t
# i
# g
# a
# b
# r
# i
# e
# l
# i

foods = ["khinkali", "mwvadi", "xachapuri", "xizilala", "xorci"]
x_counter = 0
for food in foods:
    for char in food:
        if char == "x": # თუ food-ის თითოეული ელემენტის [0] ინდექსზე მყოფი სიმბოლო გაუტოლდება "x"-ს
            x_counter += 1 
print(x_counter)
# დაიპრინტება 3,char ცვლადი შეამოწმებს food სიაში თითოეული ელემენტის თითოეულ სიმბოლოს


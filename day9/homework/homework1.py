# 1 input ფუნქციით შემოატანინეთ წინადადება
# და შმოტანილ წინადედებაში პროგრამას დაათვლევინეთ თანხმოვნები

my_str = input("Enter Any Text: ")
amount_of_consonant = 0
for char in my_str:
    if char in "bcdfghjklmnpqrstvwxyz":
        amount_of_consonant += 1
print(amount_of_consonant)

# 2 way
text = input("Enter A Text: ")
vowels = "aeiouAEIOU"
amount_of_consonant = 0

for char in text:
    if char not in vowels: # თუ text-ში შეყვანილი სიმბოლოები არ უდრის ხმოვნებს
        amount_of_consonant += 1
print("Amount of consonant is " + str(amount_of_consonant))

# იპოვეთ ყველაზე პატარა რიცხვი აქ
# 1 way
my_arr = [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
print(min(my_arr))

# 2 way
my_arr = [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
my_arr.sort()
print(my_arr[0])

# 3 way
my_arr = [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
min_num = max(my_arr)
for score in my_arr:
    if score < min_num:
        min_num = score
print(min_num)

# 4 way
my_arr = [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
min_num = max(my_arr) 
i = 0
while i < len(my_arr):
    if my_arr[i] < min_num:
        min_num = my_arr[i]
    i += 1
print(min_num)

# შევქმნათ ორი List-ი ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების
# დავპრინტოთ დაწყვილებულად აი დააკომენტარეთ და დაგაწყვილებთო რო იცოდნენ ფბზე ეგრე დაახლოებით

boys = ["Rati", "Nika", "Giorgi", "Gabrieli"]
girls = ["Alison", "Nata", "Natia", "Lika"]
i = 0
for name in boys:
    print(name + " loves " + girls[i])
    i += 1
# დაიპრინტება 
# Rati loves Alison
# Nika loves Nata
# Giorgi loves Natia
# Gabrieli loves Lika

# 2 way
girls_list = [] # ცარიელი სია
boys_list = []

for i in range(4):
    girls_name = input("Enter Girls Name: ")
    boys_name = input("Enter Boys Name: ")

    girls_list.append(girls_name) # girls-list-ში დაემატოს girls_name-იდან input-ით შეყვანილი სახელები
    boys_list.append(boys_name)
    i = 0
    for name in girls_list:
        print(name + " loves " + boys_list[i])
        i += 1

# შექმენით ნებისმიერი რიცხვების სია და დაპრინტეთ მხოლოდ დადებითი რიცხვების ჯამი

numbers = [21,-3,30,7,56,12]
my_sum = 0
for num in numbers:
    if num > 0:
        my_sum += num
print(my_sum)

# 2 way
my_list = []
my_sum = 0

for i in range(5):
    numbers = int(input("Enter A Num: "))
    my_list.append(numbers)

    for num in my_list:
        if num > 0:
            my_sum += num
print(my_sum)
print(my_list)



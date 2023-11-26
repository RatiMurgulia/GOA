my_str = "hello world"
my_arr = my_str.split() #  my_arr = ["hello", "world"]
print(my_arr)
# დაიპრინტება ['hello', 'world']

str1 = my_arr[0] # "hello"
str2 = my_arr[1] # "world"
print(str1,str2)
# დაიპრინტება hello world

my_arr = ["rati", "gabrieli", "nika", "ika"]
x = "/".join(my_arr)
print(x)
# დაიპრინტება rati/gabrieli/nika/ika
# join() ფუნქციამ ჩვენს სიაში თითოეული ელემენტებს შუა ჩასვა ჩვენს მიერ გადაცემული სიმბოლო "/"

my_arr = ["rati", "gabrieli", "nika", "ika"]
x = "/".join(my_arr[1]) # "gabrieli"
print(x)
# დაიპრინტება g/a/b/r/i/e/l/i რადგან my_arr-დან ავიღეთ [1] ინდექსზე მდგომი ელემენტი

name = "rati"
print(name.capitalize()) # Rati
# დაიპრინტება Rati

name = "rati"
upper_name = name.upper() # RATI
cap_name = name.capitalize() # Rati

print(upper_name)
print(cap_name)
# დაიპრინტება
# RATI
# Rati

my_arr = ["nika", "rati", "gio", "mari", "nini"]
gio_index = my_arr.index("gio")

print(gio_index)
# დაიპრინტება 2 რადგან index() ფუნქციაში გადაცემული ელემენტი "gio" იდგა [2] ინდექსზე

name = "rati"
t_index = name.index("t")
print(t_index)
# დაიპრინტება 2 რადგან სიმბოლო "t" name-ში იდგა [2] ინდექსზე
# index() ფუნქცია ყოველთვის პოულობს პირველივე ინდექსზე მდგომი ელემენტის ინდექს

name = "rati"
name_upper = name[2].upper()
print(name_upper)
# დაიპრინტება T რადგან name-ში მივწვდით [2] ინდექსზე მდგომ სიმბოლოს და upper() ფუნქციით გავადიდეთ ეს სიმბოლო

for i in name:
    if i == "t":
        i = i.upper()
    print(i)
# დაიპრინტება
# r
# a
# T
# i

name = "rati"
print(name.replace("t", "T")) # 1) "t" რას ვანაცვლებთ 2) "T" რა სიმბოლოთი ვანაცვლებთ
# დაიპრინტება raTi
# replace() ფუნქციით ჩავანაცვლეთ ელემენტი







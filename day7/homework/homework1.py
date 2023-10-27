# შექმენით სია სადაც გადასცემთ რაზმის ლიდერების სახელს და გვარს ელემენტებად
# გამოიტანეთ თქვენი რაზმის ლიდერის სახელი

my_arr = ["Molodini", "Djanezashvili", "Tkheshelashvili", "Philishvili"]
for element in my_arr:
    if element == "Molodini":
        print(element)

my_arr = ["Molodini", "Djanezashvili", "Tkheshelashvili", "Philishvili"]
print(my_arr[0])

my_arr = ["Molodini", "Djanezashvili", "Tkheshelashvili","Philishvili"]
new_arr = []
for i in my_arr:
    if i == "Molodini":
        new_arr.append(i)
print(new_arr)

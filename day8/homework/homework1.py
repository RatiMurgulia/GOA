# შექმენით სია ამ სიაში ჩაწერეთ სხვადასხვა რიცხვები და გამოიტანეთ ამ სიაში ყველა რიცხვების ჯამი
# ასევე ამ სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე ლუწია თუ კენტი

my_arr = [17,25,7,24,15,5,76,3]

i = 0
while i < len(my_arr):
    print(my_arr[i] + my_arr[i])
    i += 1
    
my_arr = [17,25,7,24,15,5,76,3]

my_sum = 0
for num in my_arr:
    my_sum += num
print(my_sum)

my_arr = [17,25,7,24,15,5,76,3]
for num in my_arr:
    if num % 2 == 1:
        print(str(num) + " number is Odd")
    else:
        print(str(num) + " number is Even")


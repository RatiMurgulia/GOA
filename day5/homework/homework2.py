# 0-დან 30-ის ფარგლებში დაპრინტეთ ყველა კენტი და ლუწი რიცხვი
# გვერდით მიუწერეთ კენტია თუ ლუწი რიცხვი

# პირველი მეთოდი

for i in range(30):
    if i % 2 == 0:
        print("რიცხვი " + str(i) + " არის ლუწი")
    if i % 2 == 1:
        print("რიცხვი " + str(i) + " არის კენტი")

# მეორე მეთოდი

num1 = 1
num2 = 2

for i in range(10):
    if num1 >= 0:
        print(str(num1) + " is odd")
        print(str(num2) + " is even")
    num1 = num1 + 2
    num2 = num2 + 2
    i += 1

# მესამე მეთოდი

even = 2
odd = 1
while even <= 10:
    print(str(odd) + " is odd")
    print(str(even) + " is even")
    even = even + 2
    odd = odd + 2

# მეოთხე მეთოდი

i = 1
while i < 10:
    print(i, " is odd")
    print(i + 1, " is even")
    i += 2

# 0-დან 30-ის ფარგლებში დაპრინტეთ ყველა კენტი და ლუწი რიცხვი
# გვერდით მიუწერეთ კენტია თუ ლუწი რიცხვი

for i in range(30):
    if i % 2 == 0:
        print("რიცხვი " + str(i) + " არის ლუწი")
    if i % 2 == 1:
        print("რიცხვი " + str(i) + " არის კენტი")

# 2 way
num1 = 1
num2 = 2

for i in range(10):
    if num1 >= 0:
        print(str(num1) + " is odd")
        print(str(num2) + " is even")
    num1 += 2
    num2 += 2

# 3 way
even = 2
odd = 1
while even <= 10:
    print(str(odd) + " is odd")
    print(str(even) + " is even")
    even += 2
    odd += 2

# 4 way
i = 1
while i < 10:
    print(i, " is odd")
    print(i + 1, " is even")
    i += 2

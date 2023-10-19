# მომხმარებელს შემოატანინეთ სახელი
# და დაპრინტეთ ეს სახელი იმდენჯერ რამდენი სიმბოლოც არის სახელში

name = input("Enter Your Name: ")

for i in range(len(name)):
    print(str(i) + " " + name)
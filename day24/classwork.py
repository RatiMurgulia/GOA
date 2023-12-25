# format() function
name = input("Enter your name: ")
age = input("Enter your age: ")
result = "My name is {} and my age is {} years old".format(name,age)
print(result)

# 2 way format() fuction
result2 = f"my name is {name} and i am {age} years old"
print(result2)


# binary system ორობითი სისტემა
binary = 111001 # binary სისტემაში ათვლა იწყება მარჯვნიდან


# count() function
list = [1, 4, 6, 3, 1, 2, 4, 6]
count_ones = list.count(1) # count(1) ფუნქციას გადავეცით სიაში მყოფი 1-იანი ელემენტი
# რომელსაც ის დათვლის და დაგვიწერს თუ რამდენი 1-იანია სიაში
print(count_ones)


# match function
def planet(id): # match keyword-ს გადაეცემა არგუმენტი მაგ. id-ი რომელიც def() ფუნქციის პარამეტრად გვაქვს გადაცემული
    name = ""

    match id:
        case 1: # მაგ. case თუ იქნება გადაცემული 1-იანის ტოლი
            name = "Mercury" # name ცვლადს გადაეცემა მნიშვნელობად Mercury
        case 2:
            name = "Venera"
        case 3:
            name = "Earth"
    print(name) # ვპრინტავთ სახელს
planet(2) # ვწერთ ფუნქციის პარამეტრის სახელს planet-ს და გადავცემთ არგუმენტად რაიმე რიცხვს მაგ. 2
# დაიპრინტება Venera რადგან case 2 შესრულდა

# ასევე შეგვიძლია case-ებში დავწეროთ სიტყვებიც
def georgian_food(sachmeli):
    name = ""

    match sachmeli:
        case "megruli sachmeli":
            name = "xarcho"
        case "megruli sasmeli":
            name = "arayi"
    print(name)
georgian_food("megruli sasmeli")

# input() ით
name = input("Enter Name: ")
def information(name):
    match name:
        case "goa":
            print("tqven shexvedit goa-shi")
information(name)


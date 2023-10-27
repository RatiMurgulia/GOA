# დაწერეთ პროგრამა რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას
# ენდომად გამოიძახებთ ერთ ჯგუფელს თუ კითხვაზე უპასუხებს მოემატება 10 ქულა და გადავალთ შემდეგზე
# ოღონდ ეს ვეღარ უპასუხებს იმ დღეს ანუ remove დაგჭირდებათ

# answer = input("did the student answer correctly: ")
#     if answer == "yes":
#         ............ moematos 10 qula 
#         if answer == "no"
#                     daakldes 5 qula
# [11:51 AM]
# ცალკე უნდა იყოს ქულების სიაც
import random

goa_students = ["Gabrieli", "Rati", "Nika", "Gio", "Rezi", "Daviti"]
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
question = num1 + num2
answer = int(input("Enter your answer: "))
  
student = (random.choice(goa_students))
for i in range(len(goa_students)):
    student = (random.choice(goa_students))
if answer == num1 + num2:
    print("Congratulations " + student + " you have gained 10 points")
else:
    print(student + " sorry,your answer is wrong")
    goa_students.remove(student)
    new_student = (random.choice(goa_students))
    print(new_student + " are you ready? you are next")





   
    




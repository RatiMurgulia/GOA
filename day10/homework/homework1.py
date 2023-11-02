# დაწერეთ პროგრამა რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას
# ენდომად გამოიძახებთ ერთ ჯგუფელს თუ კითხვაზე უპასუხებს მოემატება 10 ქულა და გადავალთ შემდეგზე
# ოღონდ ეს ვეღარ უპასუხებს იმ დღეს ანუ remove დაგჭირდებათ

# answer = input("did the student answer correctly: ")
#     if answer == "yes":
#         ............ moematos 10 qula 
#         if answer == "no"
#                     daakldes 5 qula
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

# 2 professional way
import random

arr_of_students = ["giorgi", "rati", "salome", "anri", "demetre"]
arr_of_grades = [0, 0, 0, 0, 0]

for i in range(5):
    random_student = random.choice(arr_of_students)
    print(random_student)

    answer = input("did the student answer correctly?: ")
    index_of_random_student = arr_of_students.index(random_student)
    if answer == "yes":
        random_student_grade = arr_of_grades[index_of_random_student]
        random_student_grade += 10

        print(random_student, " has plus 10 grade and the next student is: ")
        arr_of_students.remove(random_student)

    elif answer == "no":
        random_student_grade = arr_of_grades[index_of_random_student]
        random_student_grade -= 5
        print("the student has minus 5 grade and the next student is: ")
    else:
        print("yes or no?: ")
print("quiz is over and the student have overall grade ", arr_of_grades)





   
    




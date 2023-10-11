# my_age = int(input("Enter Your Age: ")) # 27
# fathers_age = int(input("Enter Your Fathers Age: ")) # 49
# year = int(input("Enter Year: ")) # 2023

# for i in range(60):
#     print(str(year + i) + " წელს მამაჩემი ჩემზე იქნება " + str((fathers_age + i) / (my_age + i)) + " - ჯერ დიდი")

# even = 2
# odd = 1

# while even <= 30:
#     print(str(odd) + " odd")
#     print(str(even) + " even")
#     even = even + 2
#     odd = odd + 2

# i = 1
# while i < 30:
#     print(i+2)
#     i += 3

# num1 = 20
# num2 = 20
# print(num1 != num2)

# age = 7
# if age < 18:
#   print("Junior discount")
# elif age >= 75: 
#   print("Senior discount")
# else:
#   print("No discount")
# print("Proceed to payment")

age = 16
is_student = False

if age < 18:
  #execute if age is less than 18
  if is_student:
    #execute if under 18 and also a student
    print("20% discount")
  else:
    #execute if under 18 and not a student
    print("10% discount")
else:
  #execute this code customer 18 or over
  print("Regular price")
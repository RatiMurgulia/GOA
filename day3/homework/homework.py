my_name = input("Enter your name: ")
my_surname = input("Enter your surname: ")
my_age = int(input("Enter your age: "))
my_height = float(input("Enter your height: "))

print("My name is "+ my_name+",","my surname is " + my_surname+","+"my age is " + 
       str(my_age)+","+"and my height is " + str(my_height))

year = int(input("Enter year: "))
new_age = year + (my_age)

print("after 25 yers I'm now " + str(new_age) + " years old")
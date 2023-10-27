# comparison შედარება
# conditional პირობითი
# followed მოყვა

age = 16
if age >= 18:
  print("Regular Price")
else:
  print("Discount")
# დაიპრენტება discount

age = 30
if age >= 18:
  print("Regular price")
else:
  print("Discount")
print("proceed to payment")
# დაიპრინტება Regular price და proceed to payment

num1 = 20
num2 = 10
print(num1 != num2) # != ნიშნავს არ უდრის
# დაიპრინტება True

is_student = True
age = 20
print(is_student or (age < 18))
# დაიპრინტება True
# or-ის გამოყენების დროს რომელიმე პირობა მაინც უნდა იყოს სწორი

is_student = False
age = 16
print(is_student and (age < 18))
# დაიპრინტება False
# and-ის გამოყენების დროს ორივე პირობა უნდა იყოს სწორი

age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else:
  print("Regular price")
# დაიპრინტება Discount რადგან ერთ-ერთი პირობა არის სიმართლე

age = 16
if age < 18: print("Apply Discount") # print-ის დაწერა შეგვიძლია ერთ ხაზში
print("proceed to Payment")
# დაიპრინტება Apply Discount და proceed to Payment

age = 75
if age < 18:
  print("Junior discount")
elif age >= 75: # elif არის იგივე if,უბრალოდ if-ის პირობის გაგრძელებაა.
  print("Senior discount")
else:
  print("No discount")
print("Proceed to payment")

age = 20
if age < 18:
  print("Junior didcount")
elif age >= 75:
  print("Senior discount")
else:
  print("No discount")
# დაიპრინტება No discount

age = 16
is_student = True
if age < 18:
# execute if age is less than 18
  if is_student:
# execute if under 18 and also a student
    print("20% discount")
  else:
# execute if under 18 and not a student
    print("10% discount")
else:
# execute this code customer 18 or over
  print("Regular price")
# დაიპრინტება 20% discount
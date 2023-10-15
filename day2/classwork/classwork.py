# პროექტის github-ზე ატვირთვა თავდაპირველად
# git add .
# git commit -m "... commit"
# git branch -M main
# git push -u origin main
# პროექტის განმეორებით ატვირთვისას გვჭირდება მხოლოდ რამდენიმე ბრძანება
# git add .
# git commit -m "... commit"
# git push

# quotation mark - ნიშნავს ""-ს
book = "rati's book" # '-ს ვიყენებთ სტროფების გამოსაყოფად და ასევე სტრინგების შესაქმნელადაც
print(book)

print(type(7 + 10)) # type() საშუალებით ვამოწმებთ ობიექტების ტიპს
print(type("7" + "10"))

item = "laptop" 
# item არის ცვლადი
# = არის მნიშვნელობის მიმნიჭებელი ოპერატორი
# "" არის ცვლადის მნიშვნელობა
print("i have a " + item)  
# მივიღებთ შედეგს i have a laptop

item = "laptop"
price = 100
print("I have a " + item + " and it costs " + str(price))
# მივიღებთ შედეგს I have a laptop and it costs 100

print(7 + 3)
print(10 - 5)
print(5 * 3) # * ნიშნავს გამრავლებას
print(10 / 4) # /-ით გაყოფისას გამოაქვს ზუსტი პასუხი
print(10 // 4) # //-ით გაყოფისას გამოაქვს ჩამოჭრილი პასუხი
print(20 % 3) # %-ით გაყოფისას გამოაქვს მხოლოდ ნაშთი

# დავალება
# შექმენით თქვენი ოჯახის წევრების ასაკებისგან ცვლადები
# დაპრინტეთ ასაკები 5 წლის შემდეგ

mothers_age = 45
fathers_age = 49
sisters_age = 17

mothers_age += 5
fathers_age += 5
sisters_age += 5
print(mothers_age,fathers_age,sisters_age)

my_age = 27
my_age += 5 # გაიზარდა 5-ით
my_age = my_age + 5 # იგივე ვარიანტი
# += ნიშნავს გაზრდას
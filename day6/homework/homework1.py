# მომხმარებლის ნიშნებიდან გამოიანგარიშე საშუალო არითმეტიკული
# თუ 9-ზე მეტი იქნება დაპრინტე "გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები"
# თუ იქნება 5-ზე ნაკლები დაპრინტე "გილოცავ გაექეცი მატრიცას"
# თუ იქნება 5-დან 9-მდე დაპრინტე "YOU ARE MID"
# თუ იქნება 10-ზე მეტი ან 0-ზე ნაკლები დაპრინტე "there is something wrong with you"

user1 = int(input("Enter User1 Score: "))
user2 = int(input("Enter User2 Score: "))
user3 = int(input("Enter User3 Score: "))
user4 = int(input("Enter User4 Score: "))

users_arithmetic_average = (user1 + user2 + user3 + user4) / 4
if users_arithmetic_average > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები„")
elif users_arithmetic_average < 5:
    print("გილოცავ გაექეცი მატრიცას")
elif users_arithmetic_average >= 5 and users_arithmetic_average <= 9:
    print("YOU ARE MID")
else:
    users_arithmetic_average > 10 or users_arithmetic_average < 0
    print("there is something wrong with you")


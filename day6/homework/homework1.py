# მომხმარებლის ნიშნებიდან გამოიანგარიშე საშუალო არითმეტიკული
# თუ 9-ზე მეტი იქნება დაპრინტე "გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები"
# თუ იქნება 5-ზე ნაკლები დაპრინტე "გილოცავ გაექეცი მატრიცას"
# თუ იქნება 5-დან 9-მდე დაპრინტე "YOU ARE MID"
# თუ იქნება 10-ზე მეტი ან 0-ზე ნაკლები დაპრინტე "there is something wrong with you"

score1 = int(input("Enter Score1: "))
score2 = int(input("Enter Score2: "))
score3 = int(input("Enter Score3: "))
score4 = int(input("Enter Score4: "))

avg_score = (score1 + score2 + score3 + score4) / 4
if avg_score > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები„")
elif avg_score < 5:
    print("გილოცავ გაექეცი მატრიცას")
elif avg_score >= 5 and avg_score <= 9:
    print("YOU ARE MID")
else:
    print("there is something wrong with you")

# 2
total_score = 0
total_num = 0
for i in range(5):
    scores = int(input("Enter Your Score: "))
    total_score += scores # იგივეა რაც total_score = total_score + scores
    total_num += 1 # იგივეა რაც total_num = total_num + 1
avg_score = total_score / total_num

if avg_score > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები„")
elif avg_score < 5:
    print("გილოცავ გაექეცი მატრიცას")
elif avg_score >= 5 and avg_score <= 9:
    print("YOU ARE MID")
else:
    print("there is something wrong with you")





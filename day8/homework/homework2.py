# ბილეთი ღირს 25 ლარი მაგრამ ბავშვებისთვის უფასოა
# გვყავს 13 ადამიანი აქედან 10 დიდი და 3 ბავშვი
# გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 

ammount_of_kids = 0
ammount_of_adults = 0
total_cost = 0
for i in range(5):
    age = int(input("Enter Your Age: "))
    if age > 18:
        print("25 GEL")
        ammount_of_adults += 1
        total_cost += 25
        print("The sum will be payable " + str(total_cost) + " GEL")
    elif age <= 18 and age > 0:
        print("0 GEL")
        ammount_of_kids += 1
    else:
        print("Are You Human?")
print("There are " + str(ammount_of_adults) + " Adults and " + str(ammount_of_kids) + " Kids")
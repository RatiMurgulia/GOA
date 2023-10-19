# მომხმარებელს კითხეთ თავისი მამის ასაკი
# დაპრინტეთ ყოველ წელს რამდენით დიდი იქნება მამამისი მასზე

my_age = int(input("Enter Your Age: ")) # 27
fathers_age = int(input("Enter Your Fathers Age: ")) # 49
year = int(input("Enter Year: ")) # 2023

for i in range(60):
    print(str(year + i) + " წელს მამაჩემი ჩემზე იქნება " + str(fathers_age + i - my_age) + " წლით დიდი")

# მომხმარებელს კითხეთ თავისი მამის ასაკი
# დაპრინტეთ ყოველ წელს რამდენჯერ უფროსი იქნება მამამისი მასზე

my_age = int(input("Enter Your Age: ")) # 27
fathers_age = int(input("Enter Your Fathers Age: ")) # 49
year = int(input("Enter Year: ")) # 2023

for i in range(10):
        print(str(year + i) + " წელს მამაჩემი ჩემზე იქნება " + str((fathers_age + i) / (my_age + i)) + " - ჯერ დიდი")

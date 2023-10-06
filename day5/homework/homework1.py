my_age = int(input("Enter Your Age: ")) # 27
fathers_age = int(input("Enter Your Fathers Age: ")) # 49
year = int(input("Enter Year: ")) # 2023

for i in range(60):
    print(str(year + i) + " წელს მამაჩემი ჩემზე იქნება " + str(fathers_age + i - my_age) + " წლით დიდი")
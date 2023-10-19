# Sequences მიმდევრობა
# Iterations განმეორება
# Selection არჩევა
# Flowchart გვეხმარება ალგორითმების ვიზუალიზაციაში
# Pseudocode არც კოდი და არც ვიუალიზაცია
# commas ,
# colon :

for i in range(3):
    print("hello")
# დაპრინტავს 3-ჯერ hello-ს

# for არის რომლითაც იქმნება ციკლები
# i არის საიტერაციო ცვლადი
# in ნიშნავს თუ რაში მოხდეს იტერაცია
# range არის დიაპაზონი

for i in range(3):
    print(i)
# დაპრინტავს 0 1 2 მივა 3-მდე

for i in range(4):
    print(str(i) + " Rati")

# დაპრინტავს 0 Rati 1 Rati 2 Rati 3 Rati
i = 5
while i > 0: # სანამ i > 0-ზე
    print(i)
    i -= 1 #  i შემცირდა 1-ით
# დაპრინტავს 5 4 3 2 1 ზემოდა ქვემოთ

name = "rati"
i = len(name) # i = name-ის სიგრძეს
while i > 0: # სანამ i > 0-ზე
    print(i)
    i -= 1
# დაპრინტავს 4 3 2 1 რა სიგრძისაც არის name ცვლადის მნიშვნელობა ანუ "rati"

# seat სავარძელი
seats = 5
while seats > 0:
    print(str(seats) + " Sell Ticket")
    seats = seats - 1 # ან seats -= 1 გამოაკლდეს შემცირდეს 1-ით
# დაპრინტავს
# 5 Sell Ticket
# 4 Sell Ticket
# 3 Sell Ticket
# 2 Sell Ticket
# 1 Sell Ticket
from turtle import * # პითონის ერთ ერთი ბიბლიოთეკა turtle



# we want to paint house


# step 1 draw a square

shape("turtle") # კუს გამოსახულების შემოტანა ისრის მაგივრად
speed(30) # ხატვის სისწრაფე
width(7) # ხაზის სისქე
color("red") # ხაზის ფერის მიცემა

forward(200) # წინ წასვლა, 200 ნიშნავს თუ რამდენი პიქსელით უნდა წავიდეს წინ
left(90) # მოხვევა,90 ნიშნავს მოხვევის გრადუსს
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
# and of square

# drawing a door

forward(70)
color("black")
begin_fill() # გაფერადების დაწყება
left(90)
forward(120)
right(90) # მოხვევა,90 ნიშნავს მოხვევის გრადუსს
forward(60)
right(90)
forward(120)
end_fill() # გაფერადების დასრულება

penup() # კალამის აღება სახატავიდა
goto(200, 200)
pendown() # კალამის ჩამოშვება სახატავიდან

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# drawing a left window

color("red")
pendown()
goto(0, 0)
right(150)
forward(160)
begin_fill()
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()

# drawing a right window

pendown()
goto(0, 0)
right(180)
forward(200)
begin_fill()
left(90)
forward(160)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

exitonclick() # გამოვა გრაფიკული ნახაზი და გათიშება მაშინ როცა დავაკლიკებთ
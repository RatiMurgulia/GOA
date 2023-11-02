# turtle-თი რენდომ რიცხვებით დახაზეთ შედევრი  
# forward(random.randint(100))

from turtle import * # turtle ბიბლიოთეკიდან ვაიმპორტებთ ყველა ფუნქციას
import random # random შემოტანა
speed(100) # სიჩქარე
width(random.randint(1,10)) # სისქე 1-დან 10-მდე
colors = ["red", "green", "blue", "purple", "yellow"] # ფერების სია
for i in range(10000): # for ციკლი 10000-მდე
    color(random.choice(colors)) # ფერების random არჩევა colors-სიიდან
    forward(random.randint(0,100)) # წინ random არჩევა 0-დან 100-მდე
    left(random.randint(0, 100)) # მარცხნივ random არჩევა 0-დან 100-მდე

exitonclick()
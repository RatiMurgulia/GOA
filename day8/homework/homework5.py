# დაპრინტეთ hello world (ოღონდ არა ასე print("hello world")

my_str = input("Enter Any Text: ")
print(my_str)

my_arr = ["my str", "any text", 5, "Hello", "python", "World", "programing"]
print(my_arr[3] + " " + my_arr[5])


my_arr = ["my str", "any text", 5, "Hello", "python", "World", "programing"]
for i in my_arr:
    for j in my_arr:
        if i == "Hello" and j == "World":
            print(i + " " + j)
        

    
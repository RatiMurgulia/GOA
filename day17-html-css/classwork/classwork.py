# This function counts how many times a character appears in the string
def str_count(str, my_char): # we defined a function name
    counter = 0
    for char in str: # we did a for loop in our string
        if char == my_char: # we check if our variable "my_char" equals to iteration variable "i"
            counter += 1 
    return counter
print(str_count("mariami","a"))


           

my_list = ["xinkali", "mwvadi", "vashli"]
print(my_list)
# დაიპრინტება ['xinkali', 'mwvadi', 'vashli']

my_list = ["xinkali", "mwvadi", "vashli", 7, 2.5]
print(my_list)
# დაიპრინტება ['xinkali', 'mwvadi', 'vashli', 7, 2.5]

# შეგვიძლია შევქმნათ სია ქვემოთ ჩაყოლებით
fruits = [
"apple",
"banana",
"mango",
"orange"
]
print(fruits)
# დაიპრინტება ['apple', 'banana', 'mango', 'orange']

print("Hello \nWorld")
# დაიპრინტება
# Hello 
# World
# \n new line-საშუალებით World-ი გადავიტანეთ ქვემოთ ახალ ხაზში
print("Hello \tWorld")
# დაიპრინტება Hello   World \t-ის საშუალებით Hello დავაშორეთ 4 space-ით World-ს

animals = ["cat", "dog", "bird"]
print(animals[0])
# დაიპრინტება cat რადგან 0 ინდექსზე დგას,სიაში დათვლა იწყება 0-დან.

my_list = ["xinkali", "mwvadi", "vashli", 7, 2.25]
print(my_list[0][1])
# დაიპრინტება i სიმბოლო რადგან 0 ინდექსზე დგას "xinkali" და მასში პირველ ინდექსზე დგას i სიმბოლო

animals = ["cat", "dog", "bird"]
print(animals[0] + animals[2])
# დაიპრინტება cat bird რადგან ინდექსების გამოყენებით მოვახდინეთ ელემენტების შეერთება

last_call = ["Mom", "Dave", "Lawyer"]
print(last_call[0])
print(last_call[1])
# დაიპრინტება
# Mom
# Dave

last_call = ["Mom", "Dave", "Lawyer"]
print(last_call[0],last_call[1],last_call[2])
# დაიპრინტება Mom Dave Lawyer კვადრატული ფრჩხილებისა და მძიმის გარეშე

animals = ["cat", "dog", "bird"]
my_pet = animals[1] # my_pet-ს მივანიჭეთ animals[1] ინდექსზე მდგომი ელემენტის მნიშვნელობა
print(my_pet)
# დაიპრინტება dog

nums = [8, 6, 19]
nums[0] = 1 # nums-ის 0 ინდექსზე მდგომი ელემენტი 8 შეიცვალა 1 იანით
print(nums)
# დაიპრინტება [1, 6, 19] 8 შეიცვალა 1 იანით

products = ["apples", "oranges", "bananas"]
products[2] = "lime"
print(products)
# დაიპრინტება ['apples', 'oranges', 'lime']

words = ["rise", "sun", "glasses"]
print(words[1] + words[0])
# დაიპრინტება sunrise შეერტებულად
print(words[1],words[0])
# დაიპრინტება sun rise დაშორებით

nums = [4, 7, 13, 3, 5]
print(nums[1] + nums [2])
# დაიპრინტება 20 რადგან სიაში შედგა მათემატიკური ოპერაცია

name = ["rati", "mari", "lili"]
new_arr = [] # ახალი ცარიელი სია
new_arr.append(name[1]) # დავამატეთ name-სიის [1] ინდექსზე მდგომი ელემენტი new_arr-ში ახალ სიაში
print(new_arr) # დავპრინტეთ ახალი სია
# დაიპრინტება ['mari'] name-სიიდან აღებული [1] ინდექსზე მდგომი ელემენტი ჩავსვით new_arr-ში append() ფუნქციის გამოყენებით

name = ["rati", "mari", "lili"]
name.append("nika")
print(name)
# დაიპრინტება ['rati', 'mari', 'lili', 'nika'] ბოლოში დაემატა "nika"

nums = [8, 6, 19, 7,16]
print(nums[1:3]) # 1 დან 3-მდე start finish
# დაიპრინტება [6, 19]
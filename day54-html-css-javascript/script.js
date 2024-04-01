let name = "gabrieli"
const surname = "molodini"
var adress = "pasanauri"
let num = 12

console.log()

// or - ||
// and - &&
if(name == "gabrueli" || name == "cotne"){
    console.log(true)
}else if(num > 10 && num < 15){
    console.log(true)
}

// while loop
// ++ 1-ით გაზრდა increment
// -- 1-ით შემცირება decrement
let i = 0
while(10 > i){
    i ++
    console.log(i + " " + "I love You")
}

// for loop
// let i = 0
for(let i=0; i < 10 ; i++){  // 1)საიკრემენტაციო ცვლადი, 2)condition თუ რა პირობა მოხდეს, 3)increment გაზრდა
     console.log(i)
}


let name = "gabrieli"
for(let i=0; i < name.length; i++){
    console.log(name[i])
}


// prompt("Enter your number: ") prompt()-ს გამოაქვს ფანჯარა სადაც შეგვყავს მონაცემი
let num = prompt("Enter your number: ")

for(let i=0; i < num; i ++){
    if(i % 2 == 0){
        console.log(i)
    }
}

// მომხმარებელეს უნდა შემოატანინოთ რიცხვი, შემდეგ დაბეჭდოთ კენტია თუ ლუწი.
let num = prompt("Enter your number: ")

for(let i = 0; i < num; i ++){
    if(i % 2 == 0){
        console.log(i + " is Even")
    }else{
        console.log(i + " is Odd")
    }
}

//  Homework

// 1) მოხმარებელი შემოიტანს რიცხვს, თუ ის იქნება უარყოფითი რიცხვი უნდა დაგვიბრუნოს უარყოფითი რიცხვი, თუ ის იქნება დადებითი რიცხვი დაგვიბრუნოს   უარყოფითი რიცხვი, ყველა შემთხვევაში გვიბრუნებს უარყოფით რიცხვს გარდა ნულისა
let userNumber = prompt("Enter your number: ")
if(userNumber <= 0){
    console.log("userNumber")
}else{
    console.log(userNumber * -1)
}


// 2) მომხამრებელს შემოატანინეთ რიცხვი შემდეგ კი დაბეჭდეთ მომხმარებლის შემოტანილ რიცხვამდე ყველა რიცხვის ჯამი
let userNumber = Number(prompt("Enter Your Number: "))
let sum = 0 // 20

for(let i=0; i <= userNumber; i++){
    sum += i
}
console.log(sum)
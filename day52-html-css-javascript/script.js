// ცვლადები

// var - variable - ცვლადი
var name = "gabrieli" // ცვლადის შექმნა
console.log(name) // კონსოლში გამოტანს შედეგს

// camel case style
let myName = 'rati' // let არის ცვლადის ახალი ვერსია რომელიც უფრო გამოყენებადია
let myAge = 10
console.log(myName + myAge) // კონსოლში გამოიტანს შედეგს rati10,javascript-ში string-ი და integer-ი ერთმანეთს ემატება!


let floatNumber = 10.5
let isAccepted = true // boolean-ი javascript-ში იწყება პატარა სიმბოლოთი

console.log(typeof myName) // typeof ცვლადების ტიპის შემოწმება
console.log(typeof floatNumber) // interger-ს და float-ს აქვს ერთი ტიპი ორივე არის number-ი

console.log('My name Is ' + myName)

// const-constant არის შეუცვლელი ცვლადი რომელსაც ახალ მნიშვნელობას ვერ მივცემთ
const num1 = 5
console.log(num1)

// execise
let myName = 'rati'
let myAge = 28
const myDay = 7
console.log(myName + myAge + myDay)

let num = '5'
let sum = num + 5
console.log(typeof sum) // string


// if else
let age = 9

if(age < 5){
    console.log('age < 5-ze')
}else if(age < 18){ // else if იგივეა რაც else
    console.log('age < 18-ze')
}else{
    console.log('tolia')
}


console.log(5 == '5') // true
console.log(5 === '5') // იქნება false რადგან === არის მკაცრი ტოლობა


if('5' === 5){
    console.log('true')
}else{
    console.log('false')
}

let text = 'hello world'
console.log(text.length) // length ელემენტის სიგრძის გაგება


let num1 = '5'
let num2 = Number(num1)
let num3 = String(num2)

console.log(typeof num1)
console.log(typeof num2)
console.log(typeof num3)

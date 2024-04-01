//

// input: 5
// output: -5
let userNumber = prompt("Enter your number: ")
if(userNumber <= 0){
    console.log("userNumber")
}else{
    console.log(userNumber * -1)
}

let userNumber = Number(prompt("Enter your number: ")) // შემოტანილი string-ი გადავაქციეთ რიცხვად
userNumberIncrement = userNumber + 10
while(userNumber < userNumberIncrement){
    console.log(userNumber)
    userNumber++
}

//
let num = 0
for(let i = 0; i < 10; i++){
    num = i
    console.log(num)
}


// homework 2
let userNumber = Number(prompt("Enter Your Number: "))
let sum = 0 // 20

for(let i=0; i <= userNumber; i++){
    sum += i
}
console.log(sum)


// function
// alert("Hello") // alert-ი საიტის ჩართვისას გვატყობინებს ჩვენს მიერ გადაცემულ სტრიქონს

// function magaziisGza(){ // შევქმენით ფუნქცია
//     console.log("გახვედი სახლიდან")
//     console.log("გაუხვიე მარჯვნივ")
//     console.log("წახვედი პირდაპირ")
//     console.log("ჩაირბინე ქვემოთ")
//     console.log("გაუხვიე მარცხნივ")
//     console.log("წახვედი პირდაპირ")
//     console.log("დაინახე მაღაზიან")
//     console.log("გააღე კარები")
//     console.log("შეხვედი მაღაზიაში")
//     console.log("გააღე კარები")
//     console.log("იყიდე პური")
//     console.log("წახვედი სახლში")
// }
// magaziisGza() // გამოვიძახეთ ჩვენს მიერ შექმნილი ფუნქცია


function multiply(){
    let num1 = prompt("enter num1: ")
    let num2 = prompt("enter num2: ")
    alert("ამ რიცხვების ნამრავლი არის " + num1 * num2)
}
multiply()

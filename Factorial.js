// Factorial using for Loop With Function

function calc(num){
    factorial = 1;
    for( let i = 1; i <= num; i++){
    factorial = factorial*i;
    }
    return factorial
}

let result = calc(10)
console.log(result);


// Factorial using While Loop

let a = 1;
let fact = 1;
while( a <= 10 ){
    fact = fact*a;
    console.log(fact);
    a++;
}

// Factorial using for Loop 

// factorial = 1;
// for( let i = 1; i <= 10; i++){
//     factorial = factorial*i;
//     console.log(factorial);
// }

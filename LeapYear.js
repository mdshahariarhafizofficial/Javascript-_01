// Leap Year Check

function checkLeapYear (year){
    if((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0)){
        console.log("Given Year is Leap year");
    }else{
        console.log("Given Year is Not Leap year");
    }
}

checkLeapYear(1970)
const number = Number(prompt("Enter a number:"));

// Define a function to check the sign of a number
if (number === 0) {
    alert("The number is 0.");
}
else if (number > 0) {
    alert("The number is positive.");
}
else if (number < 0) {
    alert("The number is negative.");
}
// If the input is neither positive nor negative nor zero, alert that the input is wrong
else {
    alert("Input is wrong");
}

checkNumberSign();

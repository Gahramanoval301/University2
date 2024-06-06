// Prompt the user to enter a number and convert the input to a number
const number = Number(prompt("Enter a number: "));

// Define a function to check if a number is even or odd
function checkEvenOdd(number) {
    // Check if the number is divisible by 2
    if (number % 2 === 0) {
        alert(number + " is even.");
    } else {
        alert(number + " is odd.");
    }
}
checkEvenOdd(number);

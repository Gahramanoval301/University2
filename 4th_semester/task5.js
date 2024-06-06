// Define a function that compares two numbers x and y
function compareNumbers(x, y) {
    // comparisons of x and y
    if (x > y) {
        alert("x is greater");
    }
    else if (y > x) {
        alert("y is greater");
    }
    else if (y === x) {
        alert("equal");
    }
    // If none of the above conditions are met, it means the input is invalid
    else {
        alert("wrong input");
    }
}

let x = Number(prompt("Enter the first number:"));
let y = Number(prompt("Enter the second number:"));

compareNumbers(x, y);

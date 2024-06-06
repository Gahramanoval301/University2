function calculateCube(number) {
    let cube = number ** 3; // or you can use Math.pow(number, 3)

    // Create a new paragraph element
    let paragraph = document.createElement("p");

    // Set the text content of the paragraph to display the result
    paragraph.textContent = "The cube of " + number + " is " + cube + ".";

    // Append the paragraph to the document body (you can append it to any other element as needed)
    document.body.appendChild(paragraph);
}

let number = Number(prompt("Enter a number:"));
calculateCube(number);

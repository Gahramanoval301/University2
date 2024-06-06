function concatenateStrings(str1, str2) {
    // Concatenate the two strings
    let result = str1 + str2;

    //create paragraph and assign result to it.
    let paragraph = document.createElement("p");
    paragraph.textContent = result;

    // Append the paragraph to the document body 
    document.body.appendChild(paragraph);
}

concatenateStrings("Hello, ", "world!");

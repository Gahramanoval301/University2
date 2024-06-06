//Receive strings from user
const str1 = prompt("Enter the 1st string:")
const str2 = prompt("Enter the 2nd string:")

function concatenateStrings(str1, str2) {
  //concanate them
  let result = str1 + str2;
  alert("after concatenating:" + result);

}
concatenateStrings(str1, str2);


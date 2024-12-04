// Write a function to calculate the sum of digits of a given no.

// 1st method by no. => string => list
function calculateSum_ofDigits(x) {
  let sum = 0;
  let no_to_string = x.toString(); // to convert any values to string
  let list1 = no_to_string.split("");
  console.log(list1); // print the string to list values
  for (let i of list1) {
    sum += parseInt(i);
  }
  return `The sum of the entered digit is ${sum}`;
}
console.log("calculateSum_ofDigits1", calculateSum_ofDigits(123));

// 2nd method by dividing

function calculateSum_ofDigits2(y) {
  let b = y % 10;
  console.log(b);
  let c = Math.floor(y / 10);
  console.log(c);
  return b + c;
}
console.log("calculateSum_ofDigits2", calculateSum_ofDigits2(42));

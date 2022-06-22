// program to create a simple calculator using the if...else...if in JavaScript.
const operator = prompt(
  "Enter operator to perform the calculation ( either +, -, * or / ): "
);

// accept the number from the user through prompt box
const number1 = parseFloat(prompt("Enter the first number: "));
const number2 = parseFloat(prompt("Enter the second number: "));

let result;

// use if, elseif and else keyword to define the calculator condition in JavaScript.
if (operator == "+") {
  result = number1 + number2;
} else if (operator == "-") {
  result = number1 - number2;
} else if (operator == "*") {
  result = number1 * number2;
} else {
  result = number1 / number2;
}

// display the result of the Calculator
window.alert(" Result is: " + result);

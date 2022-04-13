#!/usr/bin/node

let numbers = 0;
const number = process.argv.slice(2);
if (number.length > 1) {
  number.sort();
  numbers = number[number.length - 2];
}
console.log(numbers);

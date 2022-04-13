#!/usr/bin/node

const number = process.argv.slice(2);
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  number.sort();
  console.log(number[number.length - 2]);
}

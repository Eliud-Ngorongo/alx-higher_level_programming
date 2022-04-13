#!/usr/bin/node

const number = process.argv[2];
const newNumber = parseInt(number);

function factoarial (newNumber) {
  if (isNaN(newNumber) || newNumber === 1) {
    return (1);
  } else {
    return (newNumber * factoarial(newNumber - 1));
  }
}

console.log(factoarial(newNumber));

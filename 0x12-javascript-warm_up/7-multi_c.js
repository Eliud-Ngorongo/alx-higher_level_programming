#!/usr/bin/node

const number = process.argv.length;
if (number === 2) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}

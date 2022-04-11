#!/usr/bin/node

const args = process.argv.length;
if (args === 2) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}

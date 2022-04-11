#!/usr/bin/node

'use strict';
const passed = process.argv[2];
if (passed === undefined) {
  console.log('No argument');
} else {
  console.log(passed);
}

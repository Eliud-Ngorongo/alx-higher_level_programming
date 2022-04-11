#!/usr/bin/node

'use strict';
let passed = process.argv[2];
if (passed === undefined) {
    console.log('No argument');
} else {
    console.log(passed);
}
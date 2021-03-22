#!/usr/bin/node

const process = require('process');

const myArray = process.argv.slice(2, process.argv.length);
if (myArray < 2) {
  console.log(0);
} else {
  console.log(myArray.sort().reverse()[1]);
}

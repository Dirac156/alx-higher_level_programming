#!/usr/bin/node

const process = require('process');

if (process.argv.length < 4) {
  console.log(0);
} else {
  console.log(process.argv.sort().reverse()[1]);
}

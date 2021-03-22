#!/usr/bin/node

const process = require('process');

function parseStringToNumber (myArray) {
  for (let i = 0; i < myArray.length; i++) {
    myArray[i] = Number(myArray[i]);
  }
  return myArray;
}

function findSecondBiggest (myArray) {
  myArray = parseStringToNumber(myArray);
  const biggest = Math.max(...myArray);
  let second = myArray[0];
  for (let i = 1; i < myArray.length; i++) {
    if (myArray[i] > second && myArray[i] !== biggest) {
      second = myArray[i];
    }
  }

  return second;
}

if (isNaN(process.argv[3])) {
  console.log(0);
} else {
  const allInput = process.argv.slice(2, process.argv.length);
  const secondBiggest = findSecondBiggest(allInput);
  console.log(secondBiggest);
}

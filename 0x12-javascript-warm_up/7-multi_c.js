#!/usr/bin/node

const strToPrint = 'C is fun';
const args = process.argv.slice(2);
const numToPrint = parseInt(args[0]);

if (numToPrint) {
  for (let iter = 0; iter < numToPrint; iter++) {
    console.log(strToPrint);
  }
} else {
  console.log('Missing number of occurrences');
}

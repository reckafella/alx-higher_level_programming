#!/usr/bin/node

const args = process.argv.slice(2);
const first = parseInt(args[0]);

if (first) {
  console.log('My number: ' + first);
} else {
  console.log('Not a number');
}

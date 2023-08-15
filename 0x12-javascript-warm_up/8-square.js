#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args[0]);

if (size) {
  for (let i = 0; i < size; i++) {
    const arr = [];
    for (let j = 0; j < size; j++) {
      arr.push('X');
    }
    console.log(arr.join(''));
  }
} else {
  console.log('Missing size');
}

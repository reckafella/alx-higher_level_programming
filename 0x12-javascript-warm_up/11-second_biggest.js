#!/usr/bin/node

const args = process.argv.slice(2);
const argsNum = args.length;

if (argsNum === 1 || argsNum === 0) {
  console.log(0);
} else {
  console.log(args.sort()[argsNum - 2]);
}

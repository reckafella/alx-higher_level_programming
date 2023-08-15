#!/usr/bin/node

const args = process.argv.slice(2);
const factorialNum = args[0];

function factorial (n) {
  if (n) {
    return (n * factorial(n - 1));
  } else {
    return (1);
  }
}

console.log(factorial(factorialNum));

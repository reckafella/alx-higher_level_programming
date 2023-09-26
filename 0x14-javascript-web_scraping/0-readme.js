#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const fileName = args[0];

fs.readFile(fileName, 'utf-8', (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(response);
});

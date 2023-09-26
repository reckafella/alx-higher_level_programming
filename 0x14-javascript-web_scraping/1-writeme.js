#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const fileName = args[0];
const stringToWrite = args[1];

fs.writeFile(fileName, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});

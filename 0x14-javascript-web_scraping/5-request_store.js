#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);
const fileName = args[1];
const requestURL = args[0];

request(requestURL, function (_err, _response, body) {
  fs.writeFile(fileName, body, 'utf-8', (_error) => {});
});

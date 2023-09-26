#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const requestURL = args[0];

request(requestURL, function (_err, response, _body) {
  console.log('code:', response.statusCode);
});

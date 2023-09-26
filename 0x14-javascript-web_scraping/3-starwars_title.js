#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const id = parseInt(args[0]);
const requestURL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(requestURL, function (_err, _response, body) {
  const jsonData = JSON.parse(body);
  console.log(jsonData.title);
});

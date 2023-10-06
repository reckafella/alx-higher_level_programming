#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const requestURL = args[0];

request(requestURL, function (_err, _response, body) {
  const users = JSON.parse(body);

  const completedJobs = {};

  for (const user of users) {
    const userID = user.userId;

    if (!completedJobs[userID]) {
      completedJobs[userID] = 0;
    }

    if (user.completed) {
        completedJobs[userID]++;
    }
  }

  console.log(completedJobs);
});

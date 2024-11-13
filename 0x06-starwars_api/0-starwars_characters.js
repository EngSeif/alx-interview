#!/usr/bin/node
const request = require('request');

const Id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${Id}`, { json: true }, async (err, res, body) => {
  if (err) {
    console.log('Error in first request:', err);
    return;
  }
  for (const charUrl of body.characters) {
    new Promise((resolve, reject) => {
      request(charUrl, (error, response, body) => {
        if (error) {
          console.log('Error in first request:', err);
          return; // Stop further execution if the error occurs
        }
        resolve(JSON.parse(body));
      });
    }).then((res) => {
      console.log(res.name);
    }).catch((err) => {
      console.log(err);
    });
  }
});

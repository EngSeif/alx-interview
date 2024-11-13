#!/usr/bin/node
const request = require('request');

const Id = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${Id}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error fetching data:', error);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  if (response.statusCode === 200) {
    // Get the list of characters
    const characters = movieData.characters;

    // Print each character URL
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.log('Error fetching character data:', error);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  } else {
    console.log('Error: Could not fetch movie data.');
  }
});
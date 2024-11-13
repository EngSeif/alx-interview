#!/usr/bin/node
const request = require('request-promise');

const Id = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${Id}/`;

async function fetchData (url) {
  try {
    const filmResponse = await request({
      url,
      json: true
    });
    const charUrls = filmResponse.characters;
    for (let i = 0; i < charUrls.length; i++) {
      const url = charUrls[i];
      const charResponse = await request({
        url,
        json: true
      });
      console.log(charResponse.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
fetchData(apiUrl);

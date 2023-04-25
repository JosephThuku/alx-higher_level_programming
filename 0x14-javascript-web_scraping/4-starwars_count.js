#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const WEDGE_ANTILLES_ID = 18;

request(API_URL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let wedgeCount = 0;
    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${WEDGE_ANTILLES_ID}/`)) {
        wedgeCount++;
      }
    });
    console.log(wedgeCount);
  } else {
    console.log('Error retrieving data from API.');
  }
});

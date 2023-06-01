#!/usr/bin/node
/* Write a script that prints all characters of a Star Wars movie */
const request = require('request');
const ip = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
request(ip + movieId, (error, response, body) => {
  if (error) return console.error(error);
  const characterIp = JSON.parse(body).characters;
  getCharacters(characterIp);
});

function getCharacters (characterIp) {
  for (let i = 0; i < characterIp.length; i++) {
    Promise(function (resolve, reject) {
      request(characterIp[i], (error, response, body) => {
        if (error) return console.error(error);
        const getName = JSON.parse(body).name;
        console.log(getName);
      });
    });
  }
}
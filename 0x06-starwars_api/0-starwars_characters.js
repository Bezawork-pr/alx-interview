#!/usr/bin/node
/* Write a script that prints all characters of a Star Wars movie */
const request = require('request');
const ip = "https://swapi-api.alx-tools.com/api/films/";
const movie_id = process.argv[2];
count = 0
request(ip + movie_id, (error, response, body) => {
  const character_ip = JSON.parse(body).characters
  for (let i = 0; i < character_ip.length; i++) {
    request(character_ip[i], (aerror, aresponse, abody) => {
      const get_name = JSON.parse(abody).name;
      console.log(JSON.parse(abody).name)
    });
  } 
}); 



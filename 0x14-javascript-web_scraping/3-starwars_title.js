#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Status code:', response.statusCode);
    return;
  }

  const info = JSON.parse(body);
  console.log(info.title);
});

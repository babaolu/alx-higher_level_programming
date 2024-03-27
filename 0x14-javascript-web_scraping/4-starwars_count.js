#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const charId = 18;
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
  let count = 0;
  const churl = 'https://swapi-api.alx-tools.com/api/people/' + charId + '/';
  for (let i = 0; i < info.results.length; i++) {
    if (info.results[i].characters.includes(churl)) count++;
  }
  console.log(count);
});

#!/usr/bin/node

const request = require('request');

const num = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Status code:', response.statusCode);
    return;
  }

  const info = JSON.parse(body);
  for (let j = 0; j < info.results[num - 1].characters.length; j++) {
    request(info.results[num - 1].characters[j], (cerror, cres, cbody) => {
      if (cerror) {
        console.error('CError:', cerror);
        return;
      }
      if (cres.statusCode !== 200) {
        console.error('CStatus code:', cres.statusCode);
        return;
      }
      const cinfo = JSON.parse(cbody);
      console.log(cinfo.name);
    });
  }
});

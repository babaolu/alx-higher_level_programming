#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const filePath = process.argv[3];

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Status code:', response.statusCode);
    return;
  }

  fs.writeFile(filePath, body, (err) => {
    if (err) {
      console.error(err);
    }
  });
});

#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
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
  const obj = {};
  for (let i = 0; i < info.length; i++) {
    if (info[i].completed) {
      if (Object.prototype.hasOwnProperty.call(obj, info[i].userId)) {
        obj[info[i].userId]++;
      } else {
        obj[info[i].userId] = 1;
      }
    }
  }
  console.log(obj);
});

#!/usr/bin/node

const fs = require('fs');

const data = process.argv[3];
const filePath = process.argv[2];

fs.writeFile(filePath, data, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

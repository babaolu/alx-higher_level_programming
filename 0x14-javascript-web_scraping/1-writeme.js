#!/usr/bin/node

const fs = require('fs');

const data = process.argv[3] + '\n';

const filePath = process.argv[2];

fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.error(err);
  }
});

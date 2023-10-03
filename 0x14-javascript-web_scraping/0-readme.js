#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

fs.readFile(args[1], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

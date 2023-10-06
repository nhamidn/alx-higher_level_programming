#!/usr/bin/node

const request = require('request');
let times = 0;
let result;

request(process.argv[2], function (_error, _response, body) {
  result = JSON.parse(body).results;

  for (let i = 0; i < result.length; ++i) {
    const characters = result[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});

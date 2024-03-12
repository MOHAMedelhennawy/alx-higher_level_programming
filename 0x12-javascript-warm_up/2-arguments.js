#!/usr/bin/node

const { argv } = require('node:process');
if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}

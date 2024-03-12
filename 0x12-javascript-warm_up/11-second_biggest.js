#!/usr/bin/node
const len = process.argv.length;
let largest = process.argv[2];
let second_largest = 0;

for (let i = 0; i < len; i++) {
  if (process.argv[i + 2] > largest) {
    second_largest = largest;
    largest = process.argv[i + 2];
  }
}

console.log(second_largest);

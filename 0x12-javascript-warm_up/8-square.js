#!/usr/bin/node
const len = parseInt(process.argv[2]);

if (len) {
  for (let i = 0; i < len; i++) {
  let row = ''
  for (let j = 0; j < len; j++) {
		  row += 'X';
	  }
  console.log(row);
  }
} else {
  console.log('Missing size');
}

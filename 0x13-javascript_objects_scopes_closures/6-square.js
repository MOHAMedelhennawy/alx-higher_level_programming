#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
	row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;

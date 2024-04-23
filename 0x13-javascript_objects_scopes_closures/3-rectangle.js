#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < x; i++) {
      row = ''
      for (let j = 0; j < h; j++) {
        row += 'X'
      }
      console.log(row)
    }
  }
}

module.exports = Rectangle;
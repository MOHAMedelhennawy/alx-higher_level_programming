#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let rectangle;

    for (let i = 0; i < this.height; i++) {
      rectangle = '';
      for (let j = 0; j < this.width; j++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }
  rotate() {
    let x;
    x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }

}
module.exports = Rectangle;

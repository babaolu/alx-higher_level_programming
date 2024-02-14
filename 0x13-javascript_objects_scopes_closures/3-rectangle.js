#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      for (let j = 0; j < this.height; j++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Rectangle;

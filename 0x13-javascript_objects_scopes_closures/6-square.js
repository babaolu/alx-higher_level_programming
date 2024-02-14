#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  charPrint (c) {
    if (this.width > 0 && this.height > 0) {
      for (let j = 0; j < this.height; j++) {
        if (!c) {
          c = 'X';
        }
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;

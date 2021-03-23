#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = this.print.bind(this);
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }
};

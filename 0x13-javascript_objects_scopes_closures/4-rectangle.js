#!/usr/bin/node

module.exports = class Rectangle {
  temp;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const array = [];
      for (let j = 0; j < this.width; j++) {
        array.unshift('X');
      }
      console.log(array.join(''));
    }
  }

  rotate () {
    this.temp = this.height;
    this.height = this.width;
    this.width = this.temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};

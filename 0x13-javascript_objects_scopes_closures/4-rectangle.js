#!/usr/bin/node

module.exports = class Rectangle {
  #temp;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // prints the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      const array = [];
      for (let j = 0; j < this.width; j++) {
        array.unshift('X');
      }
      console.log(array.join(''));
    }
  }

  rotate () {
    // exchanges the width and the height of the rectangle
    this.#temp = this.height;
    this.height = this.width;
    this.width = this.#temp;
  }

  double () {
    // multiples the width and the height of the rectangle by 2
    this.height *= 2;
    this.width *= 2;
  }
};

#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) { 
    super(size, size);
    this.size = size;
  }

  charPrint(c) {
    if (!c) {
      super.print()
    } else {
      for (let i = 0; i < this.size; i++) {
      const array = [];
      for (let j = 0; j < this.size; j++) {
        array.unshift(c);
      }
      console.log(array.join(''));
    }
    }
  }
};

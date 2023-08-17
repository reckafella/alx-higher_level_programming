#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
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

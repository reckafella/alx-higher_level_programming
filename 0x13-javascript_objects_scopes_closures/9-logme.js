#!/usr/bin/node

exports.logMe = function (item) {
  const list = [];
  list.push(item);
  let listLen = list.length;
  let itr = 0;
  

  while (itr < listLen) {
    console.log(itr + ': ' + list[itr]);
    ++itr;
  }
};

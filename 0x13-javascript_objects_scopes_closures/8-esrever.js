#!/usr/bin/node

exports.esrever = function (list) {
  const listLen = list.length;
  let iter = listLen - 1;
  const newList = [];

  while (iter >= 0) {
    newList.push(list[iter]);
    iter -= 1;
  }
  return newList;
};

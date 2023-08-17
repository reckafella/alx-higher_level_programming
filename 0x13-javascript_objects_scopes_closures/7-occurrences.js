#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const listLen = list.length;
  let nOccurs = 0;

  for (let i = 0; i < listLen; i++) {
    if (list[i] === searchElement) {
      nOccurs += 1;
    }
  }
  return (nOccurs);
};

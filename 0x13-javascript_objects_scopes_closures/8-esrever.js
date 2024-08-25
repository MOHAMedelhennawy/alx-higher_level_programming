#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const newArray = new Array(len);

  for (let i = 0; i < len; i++) {
    newArray[i] = list[len - i - 1];
  }

  return newArray;
};

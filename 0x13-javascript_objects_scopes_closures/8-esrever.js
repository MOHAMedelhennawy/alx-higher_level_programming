#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];

  for (const i in list) {
    revList[i] = list[list.length - i - 1];
  }
  return revList;
};

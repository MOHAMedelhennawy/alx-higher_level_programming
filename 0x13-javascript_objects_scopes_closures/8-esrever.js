#!/usr/bin/node
exports.esrever = function (list) {
  let rev_list = [];

  for (let i in list) {
    rev_list[i] = list[list.length - i - 1];
  }
  return rev_list;
};

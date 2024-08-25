#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(element => element === searchElement)).length;
};

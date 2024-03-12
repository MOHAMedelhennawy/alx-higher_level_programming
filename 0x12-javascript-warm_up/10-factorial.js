#!/usr/bin/node
function factorial (num) {
  let num2 = 1;
  if (num > 1) num2 = factorial(num - 1);
  return num * num2;
}

const num = process.argv[2];
if (num) {
  console.log(factorial(num));
} else {
  console.log('1');
}

#!/usr/bin/node
const count = parseInt(process.argv[2], 10);
function factorial (a) {
  if (!a || a < 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(count));

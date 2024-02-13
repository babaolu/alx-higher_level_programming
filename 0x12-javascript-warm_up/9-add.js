#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(args[2], 10), parseInt(args[3], 10)));

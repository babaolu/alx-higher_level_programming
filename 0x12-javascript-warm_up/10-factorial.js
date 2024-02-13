#!/usr/bin/node
const count = parseInt(process.argv[2], 10);
let result = 1;
if (count) {
  for (let i = 1; i <= count; i++) {
    result *= i;
  }
}
console.log(result);

#!/usr/bin/node
let count = parseInt(process.argv[2], 10);
if (!count) {
  count = 1;
}
let result = 1;
for (let i = 1; i <= count; i++) {
  result *= i;
}
console.log(result);

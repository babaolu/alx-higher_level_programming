#!/usr/bin/node
const count = process.argv;
if (count.length === 2 || count.length === 3) {
  console.log(0);
} else {
  const copy = [];
  for (let i = 0; i < count.length; i++) {
    copy.push(parseInt(count[i], 10));
  }
  copy.sort((a, b) => a - b);
  console.log(copy[copy.length - 2]);
}

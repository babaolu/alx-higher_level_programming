#!/usr/bin/node
const count = parseInt(process.argv[2], 10);
if (!count) {
  console.log('Missig size');
} else {
  for (let i = 0; i < count; i++) {
    console.log('X'.repeat(count));
  }
}

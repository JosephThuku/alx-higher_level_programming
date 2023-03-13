#!/usr/bin/node
let x = 0;
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  while (x < parseInt(args[0])){
    console.log('c is fun');
    x++;
  }
}

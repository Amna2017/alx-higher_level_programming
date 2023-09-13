#!/usr/bin/node

function findSecondBiggestInt (...args) {
  if (args.length < 2) {
    return 0;
  }
  const sortedArgs = args.map(Number).sort((a, b) => b - a);
  return sortedArgs[1];
}
const secondBiggestInt = findSecondBiggestInt(...process.argv.slice(2));
console.log(secondBiggestInt);

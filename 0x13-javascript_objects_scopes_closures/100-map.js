#!/usr/bin/node
const list = require('./100-data').list;

let cont = 0;
const arr = list.map((x) => x * cont++);
console.log(list);
console.log(arr);

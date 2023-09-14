#!/usr/bin/node
exports.callMeMoby = function (x, funct) {
  while (x && x > 0) {
    funct();
    x--;
  }
};

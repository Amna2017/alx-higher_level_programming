#!/usr/bin/node

class Rectangle {
  constructor (_width, _height) {
    if (_width > 0 && _height > 0) {
      this.width = _width;
      this.height = _height;
    }
  }

  print () {
	     let line = '';
	     for (let i = 0; i < this.height; i++) {
		           for (let j = 0; j < this.width; j++) {
				           line += 'X';
				         }
		           console.log(line);
		           line = '';
		         }
	   }
}
module.exports = Rectangle;

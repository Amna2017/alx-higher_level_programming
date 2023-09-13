#!/usr/bin/node

class Rectangle {
	  constructor (w, h) {
		      if (w > 0 && h > 0) {
			            this.width = w;
			            this.height = h;
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

	  rotate () {
		      const buffer = this.width;
		      this.width = this.height;
		      this.height = buffer;
		    }

	  double () {
		      this.width = this.width * 2;
		      this.height = this.height * 2;
		    }
}
module.exports = Rectangle;

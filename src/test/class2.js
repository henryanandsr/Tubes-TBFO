// unnamed
let Rectangle = class {
    constructor(height, width) {
      this.height = height;
      this.width = width;
    }
};
console.log(Rectangle.name); // "Rectangle"

  // named
Rectangle = class Rectangle2 {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }
};
console.log(Rectangle.name); // "Rectangle2"
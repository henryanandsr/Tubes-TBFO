function f(x = 1, y) {
    return [x, y];
}
  
f(); // [1, undefined]
f(2); // [2, undefined]
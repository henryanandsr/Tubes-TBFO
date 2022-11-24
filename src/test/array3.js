const arrayLike = {
    0: "a",
    1: "b",
    length: 2
};
console.log(Array.prototype.join.call(arrayLike, "+")); // 'a+b'
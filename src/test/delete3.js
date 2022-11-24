function Foo() {
    this.bar = 10;
}
Foo.prototype.bar = 42;
const foo = new Foo();
console.log(foo.bar); // 10
delete foo.bar; // returns true
console.log(foo.bar); // 42
delete Foo.prototype.bar; // returns true
console.log(foo.bar); // undefined
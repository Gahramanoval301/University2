function Person(name) {
    this.name = name;
}


const person = new Person('leman')
console.log(Person.toString());
console.log(Object.prototype);//+

let human = {
    name: 'leman',
    age: 18
}
console.log(human.__proto__);//+ 
console.log(human.toString()); //[Object object]
console.log(human.prototype);//-undefined
console.log(typeof(undefined), typeof(null));//Null is the object
const div = document.querySelector('.myDiv')
const h1 = document.querySelector('.myHeader')
const p = document.querySelector('.myParagraph')
h1.style.color = 'red';


const span = document.createElement('span')
span.className = 'mySpan'
span.innerHTML = `<h1 class='h1Name'>Salam</h1>`


const input = document.createElement('input')
input.setAttribute('value','enter password')

div.append(span, input)

console.log(input);
console.log(input.getAttribute('value'))
console.log(input.hasAttribute('value'))
input.className = 'myToggleInput'
input.classList.add('myInput')
console.log(input.classList.contains('myInput'),2)
input.classList.toggle('myToggleInput')




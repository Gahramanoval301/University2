const button1 = document.getElementById('button1')

const callEvent = (e) => {
    console.log(e.type, e.target, e.eventPhase);
}

button1.addEventListener("click", callEvent)
button1.removeEventListener("click", callEvent)
// button1.addEventListener("click", ()=>{
//     console.log('click');
// })
// button1.addEventListener("dblclick", ()=>{
//     console.log('dblclick');
// })
// button1.addEventListener("mousemove", ()=>{
//     console.log('mouseup');
// })

button1.addEventListener('click', (e) => {
    let keys = [];

    if (e.shiftKey) keys.push('shift');
    if (e.ctrlKey) keys.push('ctrl');
    if (e.altKey) keys.push('alt');
    if (e.metaKey) keys.push('meta');

    console.log(`Keys: ${keys.join('+')}`);
});
// addEventListener('keydown', (e) => {
//     console.log(e.key);
// }
// )
addEventListener('keypress', (e) => {
    console.log(e.key, e.code, e);
}
)
window.addEventListener('scroll', (e) => {
    console.log(e);
})
function handleSubmit(event) {
    event.preventDefault();
    console.log(event.target.value);
}
addEventListener("DOMContentLoaded", () => {
    console.log('DOM content is fully loaded');
})
addEventListener("beforeunload", () => {
    console.log('beforeunload');
})

// addEventListener("unload", ()=>{
//     console.log('unload');
// })


const backImg1 = document.getElementById('backImg1');
const lorem1 = document.getElementById('lorem1');

backImg1.addEventListener("load", () => {
    lorem1.style.color = 'green';
})

const input2 = document.getElementById('input2');
input2.addEventListener("change", (e) => {
    e.target.value = 'focus'
    e.target.style.backgroundColor = 'red'
    console.log('change');
})
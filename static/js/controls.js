


// Instrutions
let exitBtn = document.getElementById('exitBtn')
let overlayWrap = document.getElementById('instruction-wrap')
let instructionsBtn = document.getElementById('instuctionsBtn')

exitBtn.addEventListener('click', function(){
    overlayWrap.style.display = 'none'
})

instructionsBtn.addEventListener('click', function(){
    overlayWrap.style.display = 'block'
})


// Profile logout
let logoutBtn = document.getElementById('logoutBtn')
let errorWrap = document.getElementById('logout-wrap')

let yes = document.getElementById('yes-btn')
let no = document.getElementById('no-btn')
logoutBtn.addEventListener('click', function(){
    errorWrap.style.display = 'flex'
})

no.addEventListener('click', function(){
    errorWrap.style.display = 'none'
})
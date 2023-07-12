// let toggle = document.querySelector('.toggle-darkmode');
let toggle = document.querySelector('#jour-nuit');

// Turn the theme off if the 'darkmode' key exists in localStorage
if (localStorage.getItem('darkmode')) {
  document.body.classList.add('darkmode');
  toggle.innerText = 'Nuit';
}  else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.classList.add('darkmode');
    localStorage.setItem('darkmode', true);
    toggle.innerText = 'Nuit';
}

toggle.addEventListener('click', function(e) {
  e.preventDefault();
  if (document.body.classList.contains('darkmode')) {
    document.body.classList.remove('darkmode');
    toggle.innerText = 'Jour';
    localStorage.removeItem('darkmode');
  } else {
    document.body.classList.add('darkmode');
    toggle.innerText = 'Nuit';
    localStorage.setItem('darkmode', true);
  }
});

// let menuCheckbox = document.querySelector('#menuToggle');
// menuCheckbox.addEventListener('click', function(e) {
//   e.preventDefault();
//   let menu = document.querySelector('#menu');
//   if (menu.style.display != "block") {
//     menu.style.display = "block";
//   } else {
//     menu.style.display = "none";
//   }
// });

// function toggleMenu(show = false) {
//   let menu = document.querySelector('#menu');
//   if (show || menu.style.display != "block") {
//     menu.style.display = "block";
//   } else {
//     menu.style.display = "none";
//   }
// }
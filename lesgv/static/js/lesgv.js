let toggle = document.querySelector('.toggle-darkmode');


// Turn the theme off if the 'darkmode' key exists in localStorage
if (localStorage.getItem('darkmode')) {
  document.body.classList.add('darkmode');
  toggle.innerText = 'Nuit';
} 
else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
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
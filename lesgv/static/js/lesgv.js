// let toggle = document.querySelector('.toggle-darkmode');
let toggle = document.querySelector('#jour-nuit');

function lesgvGoDark(toggle) {
  localStorage.removeItem('lightmode');
  localStorage.setItem('darkmode', true);
  toggle.innerText = 'Nuit';
  document.body.classList.add('darkmode');
}

function lesgvGoLight(toggle) {
  localStorage.removeItem('darkmode');
  localStorage.setItem('lightmode', true);
  toggle.innerText = 'Jour';
  document.body.classList.remove('darkmode');
}

function toggleDarkmode() {
  let toggle = document.querySelector('#jour-nuit');
  if (document.body.classList.contains('darkmode')) {
    lesgvGoLight(toggle);
  } else {
    lesgvGoDark(toggle);
  }
}



// if (document.getElementById('menu-checkbox')) {
//   ckBox = document.getElementById('menu-checkbox');
//   if (localStorage.getItem('menuopen')) {
//     ckBox.checked=true;
//   }
//   ckBox.addEventListener('click', function(e) {
//     e.preventDefault();
//     console.log(ckBox.checked);
//     // ckBox.checked = !ckBox.checked;
//     if (ckBox.checked) {
//       localStorage.setItem('menuopen', true);
//     } else {
//       localStorage.removeItem('menuopen');
//     }
//   });
// }





toggle.addEventListener('click', function(e) {
  if (document.body.classList.contains('darkmode')) {
    lesgvGoLight(toggle);
  } else {
    lesgvGoDark(toggle);
  }
});


// Turn the theme off if the 'darkmode' key exists in localStorage
if (localStorage.getItem('darkmode')) {
  lesgvGoDark(toggle);
}  else if (localStorage.getItem('lightmode')) {
  lesgvGoLight(toggle);
} else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  lesgvGoDark(toggle);
}


window.addEventListener(
  "pagehide",
  (event) => {
    if (toggle) {
      if (document.body.classList.contains('darkmode')) {
        lesgvGoDark(toggle);
      } else {
        lesgvGoLight(toggle);
      }
    }
  },
  false,
);

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



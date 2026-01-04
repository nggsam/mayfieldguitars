/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  var navbar = document.querySelector('nav.navbar-collapse');

  if (toggleBtn && navbar) {
    toggleBtn.addEventListener('click', function() {
      // Toggle the 'in' class which controls visibility via CSS
      navbar.classList.toggle('in');
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement && typeof Headroom !== 'undefined') {
  var headroom  = new Headroom(myElement);
  headroom.init();
}

/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  var nav = document.querySelector('nav.navbar-collapse');

  if (toggleBtn && nav) {
    toggleBtn.addEventListener('click', function() {
      // Toggle the 'in' class which handles display: block vs none in CSS
      if (nav.classList.contains('in')) {
        nav.classList.remove('in');
      } else {
        nav.classList.add('in');
      }
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement && typeof Headroom !== 'undefined') {
  var headroom  = new Headroom(myElement);
  headroom.init();
}

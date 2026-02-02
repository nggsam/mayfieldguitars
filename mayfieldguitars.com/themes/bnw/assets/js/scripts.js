/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var toggle = document.getElementById('btn-toggle-nav');
  var nav = document.querySelector('nav.navbar-collapse');

  if (toggle && nav) {
    toggle.addEventListener('click', function() {
      // Toggle the 'in' class.
      // CSS transitions on max-height and visibility will handle the animation.
      nav.classList.toggle('in');
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement && typeof Headroom !== 'undefined') {
  var headroom  = new Headroom(myElement);
  headroom.init();
}

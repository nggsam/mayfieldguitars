/*
 * Optimized for performance: Vanilla JS replacement for jQuery.
 * Reduces bundle size by ~90KB.
 */

/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var toggle = document.getElementById('btn-toggle-nav');
  if (toggle) {
    toggle.addEventListener('click', function() {
      var nav = document.querySelector('nav.navbar-collapse');
      if (nav) {
        nav.classList.toggle('in');
      }
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement && window.Headroom) {
    var headroom  = new Headroom(myElement);
    headroom.init();
}

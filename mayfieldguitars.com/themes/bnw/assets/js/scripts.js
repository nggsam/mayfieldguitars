/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  var nav = document.querySelector('nav.navbar-collapse');

  if (toggleBtn && nav) {
    toggleBtn.addEventListener('click', function() {
      // Toggle the 'in' class which handles visibility via CSS
      nav.classList.toggle('in');
    });
  }

  // headroom
  var header = document.querySelector("header");
  if (header && typeof Headroom !== 'undefined') {
    var headroom = new Headroom(header);
    headroom.init();
  }
});

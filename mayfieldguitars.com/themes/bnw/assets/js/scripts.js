// Refactored to Vanilla JS
document.addEventListener('DOMContentLoaded', function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  var navbar = document.querySelector('nav.collapse');

  if (toggleBtn && navbar) {
    toggleBtn.addEventListener('click', function() {
      // Toggle the 'in' class which controls the max-height via CSS
      navbar.classList.toggle('in');
    });
  }

  // headroom
  var header = document.querySelector("header");
  if (header && typeof Headroom !== 'undefined') {
    var headroom = new Headroom(header);
    headroom.init();
  }
});

document.addEventListener('DOMContentLoaded', function() {
  /* add click event for navbar-toggle item */
  var toggleBtn = document.getElementById('btn-toggle-nav');
  var nav = document.querySelector('nav.navbar-collapse');
  if (toggleBtn && nav) {
    toggleBtn.addEventListener('click', function() {
      // Toggle the 'in' class which controls display:block/none via CSS
      nav.classList.toggle('in');
    });
  }

  // headroom
  var myElement = document.querySelector("header");
  if (myElement && window.Headroom) {
    var headroom  = new Headroom(myElement);
    headroom.init();
  }
});

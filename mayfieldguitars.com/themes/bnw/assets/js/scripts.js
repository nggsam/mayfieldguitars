document.addEventListener('DOMContentLoaded', function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  var nav = document.querySelector('nav.navbar-collapse');

  if (toggleBtn && nav) {
    toggleBtn.addEventListener('click', function(e) {
      e.preventDefault();
      nav.classList.toggle('in');
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement) {
    var headroom  = new Headroom(myElement);
    headroom.init();
}

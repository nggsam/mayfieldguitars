document.addEventListener('DOMContentLoaded', function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      var nav = document.querySelector('nav.navbar-collapse');
      if (nav) {
        nav.classList.toggle('in');
      }
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement) {
  var headroom  = new Headroom(myElement);
  headroom.init();
}

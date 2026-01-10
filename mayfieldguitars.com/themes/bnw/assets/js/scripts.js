/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-toggle-nav');
  if (btn) {
    btn.addEventListener('click', function() {
      var item = document.querySelector('nav.navbar-collapse');
      if (item) {
        item.classList.toggle('in');
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

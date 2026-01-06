/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-toggle-nav');
  var item = document.querySelector('nav.navbar-collapse');

  if (btn && item) {
    btn.addEventListener('click', function() {
      item.classList.toggle('in');
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement && typeof Headroom !== 'undefined') {
  var headroom  = new Headroom(myElement);
  headroom.init();
}

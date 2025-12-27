/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-toggle-nav');
  var item = document.querySelector('nav.navbar-collapse');

  if (btn && item) {
    btn.addEventListener('click', function() {
      // Toggle the 'in' class which controls visibility in CSS
      if (item.classList.contains('in')) {
        item.classList.remove('in');
      } else {
        item.classList.add('in');
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

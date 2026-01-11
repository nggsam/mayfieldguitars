/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-toggle-nav');
  if (btn) {
    btn.addEventListener('click', function() {
      var item = document.querySelector('nav.navbar-collapse');
      if (item) {
        // Toggle the 'in' class which controls visibility via CSS
        // .collapse.in { display: block; }
        // nav.collapse { display: none; }
        item.classList.toggle('in');
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

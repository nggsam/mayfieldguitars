/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-toggle-nav');
  if (btn) {
    btn.addEventListener('click', function() {
      var item = document.querySelector('nav.navbar-collapse');
      if (item) {
        if (item.classList.contains('in')) {
            item.classList.remove('in');
        } else {
            item.classList.add('in');
        }
      }
    });
  }
});

// headroom
var myElement = document.querySelector("header");
var headroom  = new Headroom(myElement);
headroom.init();

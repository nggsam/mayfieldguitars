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

  // headroom
  var header = document.querySelector("header");
  if (header && typeof Headroom !== 'undefined') {
    var headroom  = new Headroom(header);
    headroom.init();
  }
});

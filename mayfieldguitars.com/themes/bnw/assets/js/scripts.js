document.addEventListener('DOMContentLoaded', function() {
  /* add click event for navbar-toggle item */
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
  var myElement = document.querySelector("header");
  if (myElement && typeof Headroom !== 'undefined') {
    var headroom  = new Headroom(myElement);
    headroom.init();
  }
});

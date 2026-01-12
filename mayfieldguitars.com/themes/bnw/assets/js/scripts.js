/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      var item = document.querySelector('nav.navbar-collapse');
      if (item) {
        // Simple toggle for now, replacing slideToggle(500)
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

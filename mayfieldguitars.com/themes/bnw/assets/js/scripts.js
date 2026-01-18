/* add click event for navbar-toggle item */
document.addEventListener("DOMContentLoaded", function() {
  var toggleBtn = document.getElementById('btn-toggle-nav');
  var collapseItem = document.querySelector('nav.navbar-collapse');

  if (toggleBtn && collapseItem) {
    toggleBtn.addEventListener('click', function() {
        // Toggle the 'in' class which controls visibility via CSS
        // Replaces jQuery slideToggle + toggleClass('in')
        collapseItem.classList.toggle('in');
    });
  }
});

// headroom
var myElement = document.querySelector("header");
if (myElement && typeof Headroom !== 'undefined') {
    var headroom  = new Headroom(myElement);
    headroom.init();
}

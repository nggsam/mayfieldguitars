/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-toggle-nav');
  if (btn) {
    btn.addEventListener('click', function() {
      var item = document.querySelector('nav.navbar-collapse');
      if (item) {
        // Toggle the 'in' class
        item.classList.toggle('in');
        // Ensure no conflicting inline display property (mimicking slideToggle cleanup)
        item.style.removeProperty('display');
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

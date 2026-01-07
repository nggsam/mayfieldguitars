document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-toggle-nav');
  if (btn) {
    btn.addEventListener('click', function() {
      var item = document.querySelector('nav.navbar-collapse');
      if (item) {
        // Toggle the class 'in' to handle visibility via CSS
        // The memory explicitly states to rely on CSS for visibility changes
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
// Ensure Headroom is available before initializing
if (typeof Headroom !== 'undefined') {
    var myElement = document.querySelector("header");
    if (myElement) {
        var headroom  = new Headroom(myElement);
        headroom.init();
    }
}

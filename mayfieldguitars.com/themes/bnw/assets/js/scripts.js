/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
    var btn = document.getElementById('btn-toggle-nav');
    var nav = document.querySelector('nav.navbar-collapse');

    if (btn && nav) {
        btn.addEventListener('click', function() {
            // Toggle the 'in' class. Animation is handled by CSS in custom.css
            nav.classList.toggle('in');
        });
    }
});

// headroom
// Ensure Headroom is loaded before using it
if (typeof Headroom !== 'undefined') {
    var myElement = document.querySelector("header");
    if (myElement) {
        var headroom  = new Headroom(myElement);
        headroom.init();
    }
}

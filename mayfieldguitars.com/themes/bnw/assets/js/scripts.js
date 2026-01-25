/**
 * add click event for navbar-toggle item
 * Performance Optimization: Replaced jQuery slideToggle with Vanilla JS and CSS transitions.
 * Removes ~80KB of jQuery dependency.
 */
document.addEventListener("DOMContentLoaded", function() {
    var toggleBtn = document.getElementById("btn-toggle-nav");
    var navCollapse = document.querySelector("nav.navbar-collapse");

    if (toggleBtn && navCollapse) {
        toggleBtn.addEventListener("click", function(e) {
            e.preventDefault();
            navCollapse.classList.toggle("in");
        });
    }
});

// headroom
var myElement = document.querySelector("header");
if (myElement && typeof Headroom !== 'undefined') {
    var headroom  = new Headroom(myElement);
    headroom.init();
}

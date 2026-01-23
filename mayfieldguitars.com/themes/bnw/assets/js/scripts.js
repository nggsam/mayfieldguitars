/* add click event for navbar-toggle item */
document.addEventListener('DOMContentLoaded', function() {
    var toggle = document.querySelector('#btn-toggle-nav');
    var nav = document.querySelector('nav.navbar-collapse');

    if (toggle && nav) {
        toggle.addEventListener('click', function() {
            nav.classList.toggle('in');
        });
    }

    // headroom
    var myElement = document.querySelector("header");
    if (myElement && window.Headroom) {
        var headroom  = new Headroom(myElement);
        headroom.init();
    }
});

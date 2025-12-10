/* add click event for navbar-toggle item */
$(function() {
  $('#btn-toggle-nav').click(function() {
    var item = $('nav.navbar-collapse');
    item.slideToggle(500, function() {
      item[0].style.removeProperty('display');
      item.toggleClass('in');
    });
  });
});

// headroom
var myElement = document.querySelector("header");
var headroom  = new Headroom(myElement);
headroom.init();

// Dark Mode Toggle
$(document).ready(function() {
    var toggle = $('#dark-mode-toggle');
    var body = $('body');

    // Update button text on load based on class
    if (body.hasClass('dark-mode')) {
        toggle.text('Light Mode');
    }

    toggle.click(function(e) {
        e.preventDefault();
        body.toggleClass('dark-mode');

        if (body.hasClass('dark-mode')) {
            localStorage.setItem('theme', 'dark');
            toggle.text('Light Mode');
        } else {
            localStorage.setItem('theme', 'light');
            toggle.text('Dark Mode');
        }
    });
});

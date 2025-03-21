document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.nav');
    var currentPage = window.location.pathname;

    buttons.forEach(function(button) {
        var buttonUrl = button.getAttribute('href');

        // Check if the current page URL matches the button's URL
        if (currentPage === buttonUrl) {
            button.classList.add('active');
        }

        button.addEventListener('click', function(e) {
            buttons.forEach(function(btn) {
                btn.classList.remove('active');
            });
            e.target.classList.add('active');
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    var header = document.getElementById('header');
    var homeSection = document.getElementById('home');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > homeSection.offsetHeight) {
            header.classList.add('fixed');
        } else {
            header.classList.remove('fixed');
        }
    });
});
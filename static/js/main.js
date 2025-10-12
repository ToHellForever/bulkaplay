// Бургер-меню
document.addEventListener('DOMContentLoaded', function() {
    const burgerIcon = document.getElementById('burgerIcon');
    const menuContainer = document.getElementById('menuContainer');

    if (burgerIcon && menuContainer) {
        burgerIcon.addEventListener('click', function() {
            burgerIcon.classList.toggle('active');
            menuContainer.classList.toggle('active');
        });
    }
});


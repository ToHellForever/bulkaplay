document.addEventListener('DOMContentLoaded', function() {
  var carouselElement = document.getElementById('productCarousel');

  if (!carouselElement) {
    console.error('Карусель не найдена.');
    return;
  }

  if (typeof bootstrap === 'undefined' || typeof bootstrap.Carousel === 'undefined') {
    console.error('Библиотека Bootstrap не доступна.');
    return;
  }

  var carousel = new bootstrap.Carousel(carouselElement, {
    interval: 5000,
    wrap: true
  });

  // Улучшенная обработка для зацикливания
  carouselElement.addEventListener('slid.bs.carousel', function(event) {
    if (carouselElement.children.length > 1 && event.to === carouselElement.children.length - 1) {
      setTimeout(function() {
        carousel.to(0);
      }, 2000);
    }
  });
});
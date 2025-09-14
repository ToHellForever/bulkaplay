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

  carouselElement.addEventListener('slid.bs.carousel', function(event) {
    if (carouselElement.children.length > 1 && event.to === carouselElement.children.length - 1) {
      setTimeout(function() {
        carousel.to(0);
      }, 2000);
    }
  });
});

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


// логика товаров в форме 
$(document).ready(function () {
    // Ваш существующий JS код без изменений
    $('#id_order_type').on('change', function () {
        var selectedValue = $(this).val();
        if (selectedValue === 'buy') {
            $('#product-list').addClass('visible').removeClass('hidden');
            $('#arenda-list').addClass('hidden').removeClass('visible');
        } else if (selectedValue === 'rent') {
            $('#arenda-list').addClass('visible').removeClass('hidden');
            $('#product-list').addClass('hidden').removeClass('visible');
        }
    });

    $('#rental-type').on('change', function () {
        var rentalId = $(this).val();
        if (rentalId) {
            var selectedRental = $(this).find('option:selected');
            var maxGames = parseInt(selectedRental.data('game-count'));
            $('#max-games-count').text(maxGames);
            $('#rental-games').addClass('visible');
        } else {
            $('#rental-games').removeClass('visible');
        }
    });

    $(document).on('change', '.game-checkbox', function() {
        var checkedCount = $('.game-checkbox:checked').length;
        var maxGames = parseInt($('#max-games-count').text());
        $('#selected-games-count').text(checkedCount);
        if (maxGames > 0 && checkedCount >= maxGames) {
            $('.game-checkbox:not(:checked)').prop('disabled', true);
        } else {
            $('.game-checkbox').prop('disabled', false);
        }
    });

    function showNotification(message) {
        const container = document.querySelector('.notification-container');
        const messageEl = document.querySelector('.notification-message');
        messageEl.innerText = message;
        container.classList.remove('hidden');
        container.classList.add('show');
        setTimeout(() => {
            container.classList.remove('show');
            setTimeout(() => {
                container.classList.add('hidden');
            }, 300);
        }, 3000);
    }

    $('form').on('submit', function(event) {
        let hasSelectedItems = false;
        const orderType = $('#id_order_type').val();
        if (!orderType || orderType === 'choice') {
            event.preventDefault();
            showNotification('Выберите тип заказа.');
            return;
        }
        switch(orderType) {
            case 'buy':
                hasSelectedItems = $('input[name="selected_products"]:checked').length > 0;
                break;
            case 'rent':
                const selectedGamesCount = $('input[name="selected_games"]:checked').length;
                const maxGames = parseInt($('#max-games-count').text());
                if (selectedGamesCount !== maxGames) {
                    event.preventDefault();
                    showNotification(`Выберите ровно ${maxGames} игр для аренды.`);
                    return;
                }
                hasSelectedItems = selectedGamesCount > 0;
                break;
        }
        if (!hasSelectedItems) {
            event.preventDefault();
            showNotification('Пожалуйста, выберите хотя бы один продукт или услугу.');
        }
    });

    $('.product-item img, .game-item img').click(function() {
        const parentItem = $(this).closest('.product-item, .game-item');
        const checkbox = parentItem.find('input[type="checkbox"]');
        const isChecked = !checkbox.prop('checked');
        if (parentItem.hasClass('game-item')) {
            const checkedCount = $('.game-checkbox:checked').length;
            const maxGames = parseInt($('#max-games-count').text());
            if (isChecked && checkedCount >= maxGames && maxGames > 0) {
                return;
            }
        }
        checkbox.prop('checked', isChecked);
        if (parentItem.hasClass('game-item')) {
            const newCheckedCount = $('.game-checkbox:checked').length;
            $('#selected-games-count').text(newCheckedCount);
            if (maxGames > 0 && newCheckedCount >= maxGames) {
                $('.game-checkbox:not(:checked)').prop('disabled', true);
            } else {
                $('.game-checkbox').prop('disabled', false);
            }
        }
    });
});
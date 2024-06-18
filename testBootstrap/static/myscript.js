$('.slider-for').slick(
    {
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        dots: false,
        asNavFor: '.slider-nav'
    });
$('.slider-nav').slick(
    {
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        centerMode: true,
        focusOnSelect: true,
        responsive: [
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    dots: false
                }
            },
        ]
    });
$("[data-fancybox='gallery']").fancybox({
    buttons: [
        'slideShow',
        'share',
        'zoom',
        'fullScreen',
        'close'
    ],
    loop: true,
    protect: true,
    afterShow: function (instance, current) {
        // Обновление слайдера при открытии изображения в FancyBox
        $('.slider-for').slick('slickGoTo', current.index);
    }
});

// Обработка события клика на изображении в основном слайдере
$('.slider-for a').on('click', function (event) {
    event.preventDefault();
    var slideIndex = $(this).parents('.slick-slide').index();
    $.fancybox.open($('[data-fancybox="gallery"]'), {
        index: slideIndex
    });
});

(function ($) {
    "use strict";
    $(".hidden-content").hide();
    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Navbar on scrolling
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.navbar').fadeIn('slow').css('display', 'flex');
        } else {
            $('.navbar').fadeOut('slow').css('display', 'none');
        }
    });


    // Smooth scrolling on the navbar links
    $(".navbar-nav a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 45
            }, 1500, 'easeInOutExpo');
            
            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });
    

    // Typed Initiate
    if ($('.typed-text-output').length == 1) {
        var typed_strings = $('.typed-text').text();
        var typed = new Typed('.typed-text-output', {
            strings: typed_strings.split(', '),
            typeSpeed: 100,
            backSpeed: 20,
            smartBackspace: false,
            loop: true
        });
    }


    // Modal Video
    var $videoSrc;
    $('.btn-play').click(function () {
        $videoSrc = $(this).data("src");
    });
    console.log($videoSrc);
    $('#videoModal').on('shown.bs.modal', function (e) {
        $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
    })
    $('#videoModal').on('hide.bs.modal', function (e) {
        $("#video").attr('src', $videoSrc);
    })


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Skills
    $('.skill').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
    });

    $('#download-button').click(function() {
                // Redirect the browser to the /download-pdf route
             window.location.href = '/resume';
      });

    $("#read-more-btn").click(function() {
          $(".hidden-content").toggle();
          $(this).text(function(i, text) {
            return text === "Read More" ? "Read Less" : "Read More";
          });
        });

    $.get("https://leetcode-api-faisalshohag.vercel.app/DxBros",function(data){
            console.log(data);
            var keys = [];var values = [];
            for(var key in data){
                    if(data.hasOwnProperty(key) && typeof(data[key]) == 'number'){
                        keys.push(key);
                        values.push(data[key]);
                    }
            }
            var mapData = new Map();
            for (var i = 0; i < keys.length; i++) {
                mapData.set(keys[i], values[i]);
            }

            // Function to generate an HTML table from a Map
            function mapToTable(map) {

                var text ="<table class = 'table  table-sm table-striped table-hover'>";
                text += "<thead class='table-dark'><th> Parameters</th><th colspan='2'>Values</th></thead>";

                mapData.forEach(function(value, key) {
                    text += `<tr><td>${key}<td><td>${value}</td></tr>`
                });
                text += "</table>";
                console.log(text);
                return text;
            }

            // Get the container element and append the table
            var tableContainer = $('#leetcode-table-container');
            tableContainer[0].innerHTML = mapToTable(mapData);
    });

})(jQuery);


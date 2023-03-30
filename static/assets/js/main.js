$(function () {

    "use strict";


    //===== Prealoder
    
    $(window).on('load', function(event) {
        $('.preloader').delay(500).fadeOut(500);
    });
    

      // niceSelect 
    $(document).ready(function() {
      $('select:not(.ignore)').niceSelect();      
      FastClick.attach(document.body);

    }); 




    //===== Sticky

    $(window).on('scroll', function (event) {
        var scroll = $(window).scrollTop();
        if (scroll < 310) {
            $(".navbar-area").removeClass("sticky");
        } else {
            $(".navbar-area").addClass("sticky");
        }
        if (scroll < 310) {
            $(".toolbar-area").removeClass("d-none");
        } else {
            $(".toolbar-area").addClass("d-none");
        }
    });


    //===== Back to top

    // Show or hide the sticky footer button
    $(window).on('scroll', function (event) {
        if ($(this).scrollTop() > 600) {
            $('.back-to-top').fadeIn(200)
        } else {
            $('.back-to-top').fadeOut(200)
        }
    });


    //Animate the scroll to yop
    $('.back-to-top').on('click', function (event) {
        event.preventDefault();

        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });


  // Wow
    new WOW().init();






    //===== slick Client
    
    $('.testimonial1').slick({
       
        centerPadding: '0',
        dots: true,
        arrows: false,
        infinite: true,
        speed: 800,
        slidesToShow: 2,
        responsive: [
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: 2,
              }
            },
            {
              breakpoint: 992,
              settings: {
                slidesToShow: 2,
                centerMode: false,
              }
            },
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 1,
              }
            },
            {
              breakpoint: 576,
              settings: {
                slidesToShow: 1,
              }
            }
        ]
    });

    $('.product-carousel').slick({
       
        centerPadding: '0',
        dots: false,
        arrows: true,
        infinite: true,
        speed: 800,
        slidesToShow: 5,
        prevArrow:"<span class='prev'><i class='flaticon-left-arrow-1'></i></span>",
        nextArrow:"<span class='next'><i class='flaticon-right-arrow-2'></i></span>",

        responsive: [
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: 5,
              }
            },
            {
              breakpoint: 992,
              settings: {
                slidesToShow: 3,
                centerMode: false,
                infinite: true,
                arrows: true,
              }
            },
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 2,
                infinite: true,
                arrows: true,
              }
            },
            {
              breakpoint: 576,
              settings: {
                slidesToShow: 1,
                
                 arrows: false,
                 infinite: true,
              }
            }
        ]
    });





     //===== mobile-menu-btn
    let navbarToggler = document.querySelector(".mobile-menu-btn");
    navbarToggler.addEventListener('click', function () {
        navbarToggler.classList.toggle("active");
    });

      // Typed js
    $(".typed").typed({
        strings: ["Classifieds Ads.", " Buy, Sell, Rent.", "Exchange in one Click."],
        // Optionally use an HTML element to grab strings from (must wrap each string in a <p>)
        stringsElement: null,
        // typing speed
        typeSpeed: 30,
        // time before typing starts
        startDelay: 1200,
        // backspacing speed
        backSpeed: 20,
        // time before backspacing
        backDelay: 500,
        // loop
        loop: true,
        // false = infinite
        loopCount: Infinity,
        fadeOutDelay: 500,
        // show cursor
        showCursor: false,
        // character for cursor
        cursorChar: "|",
        // attribute to type (null == text)
        attr: null,
        // either html or text
        contentType: 'html',
        // call when done callback function
        callback: function() {},
        // starting callback function before each string
        preStringTyped: function() {},
        //callback for every typed string
        onStringTyped: function() {},
        // callback for reset
        resetCallback: function() {}
    });









});




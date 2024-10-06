/* ==============
 ========= js documentation ==========================

 * template name: Alexis
 * version: 1.0
 * description: Real Estate Html5 Template
 * author: Expert-Themes
 * author-url: https://themeforest.net/user/expert-themes

    ==================================================

     01. background image
     -------------------------------------------------
     02. custom cursor
     -------------------------------------------------
     03. preloader
     -------------------------------------------------
     04. scroll to top with progress
     -------------------------------------------------
     05. add active class to the current link
     -------------------------------------------------
     06. mobile menu
     -------------------------------------------------
     07. fixed header on scroll
     -------------------------------------------------
     08. banner one slider
     -------------------------------------------------
     09. banner two slider
     -------------------------------------------------
     10. banner four video
     -------------------------------------------------
     11. search tab
     -------------------------------------------------
     12. video popup
     -------------------------------------------------
     13. nice select
     -------------------------------------------------
     14. property slider
     -------------------------------------------------
     15. odometer counter
     -------------------------------------------------
     16. testimonial slider
     -------------------------------------------------
     17. banner tab
     -------------------------------------------------
     18. testimonial three slider
     -------------------------------------------------
     19. team slider
     -------------------------------------------------
     20. property type slider
     -------------------------------------------------
     21. partner slider
     -------------------------------------------------
     22. property tab
     -------------------------------------------------
     23. exclusive tab
     -------------------------------------------------
     24. area slider
     -------------------------------------------------
     25. exclusive slider
     -------------------------------------------------
     26. coming soon
     -------------------------------------------------
     27. countdown
     -------------------------------------------------
     28. testimonial two slider
     -------------------------------------------------
     29. explore two slider
     -------------------------------------------------
     30. property three slider
     -------------------------------------------------
     31. footer copyright year
     -------------------------------------------------
     32. aos initialization
     -------------------------------------------------
     33. gsap register
     -------------------------------------------------
     34. gsap config
     -------------------------------------------------
     35. target section with gsap
     -------------------------------------------------
     36. parallax image with gsap
     -------------------------------------------------
     37. title animation
     -------------------------------------------------
     38. lenis smooth scroll

    ==================================================
============== */

(function ($) {
  "use strict";

  jQuery(function () {
    /**
     * ======================================
     * 01. background image
     * ======================================
     */
    $("[data-background]").each(function () {
      var backgroundImages = $(this).attr("data-background").split(",");
      var cssValue = backgroundImages
        .map(function (image) {
          return 'url("' + image.trim() + '")';
        })
        .join(",");

      $(this).css("background-image", cssValue);
    });

    let device_width = window.innerWidth;
    let initialScroll = $(window).scrollTop();

    /**
     * ======================================
     * 02. custom cursor
     * ======================================
     */
    if ($(".mouseCursor").length > 0) {
      function itCursor() {
        var myCursor = jQuery(".mouseCursor");
        if (myCursor.length) {
          if ($("body")) {
            const e = document.querySelector(".cursor-inner"),
              t = document.querySelector(".cursor-outer");
            let n,
              i = 0,
              o = !1;
            (window.onmousemove = function (s) {
              o ||
                (t.style.transform =
                  "translate(" + s.clientX + "px, " + s.clientY + "px)"),
                (e.style.transform =
                  "translate(" + s.clientX + "px, " + s.clientY + "px)"),
                (n = s.clientY),
                (i = s.clientX);
            }),
              $("body").on(
                "mouseenter",
                "button, a, .cursor-pointer",
                function () {
                  e.classList.add("cursor-hover"),
                    t.classList.add("cursor-hover");
                }
              ),
              $("body").on(
                "mouseleave",
                "button, a, .cursor-pointer",
                function () {
                  ($(this).is("a", "button") &&
                    $(this).closest(".cursor-pointer").length) ||
                    (e.classList.remove("cursor-hover"),
                    t.classList.remove("cursor-hover"));
                }
              ),
              (e.style.visibility = "visible"),
              (t.style.visibility = "visible");
          }
        }
      }
      itCursor();
    }

    /**
     * ======================================
     * 03. preloader
     * ======================================
     */
    if ($(".preloader").length) {
      $(".preloader").delay(100).fadeOut(100);
    }

    /**
     * ======================================
     * 04. scroll to top with progress
     * ======================================
     */

    if ($(".progress-wrap").length > 0) {
      var progressPath = document.querySelector(".progress-wrap path");
      var pathLength = progressPath.getTotalLength();
      progressPath.style.transition = progressPath.style.WebkitTransition =
        "none";
      progressPath.style.strokeDasharray = pathLength + " " + pathLength;
      progressPath.style.strokeDashoffset = pathLength;
      progressPath.getBoundingClientRect();
      progressPath.style.transition = progressPath.style.WebkitTransition =
        "stroke-dashoffset 10ms linear";
      var updateProgress = function () {
        var scroll = $(window).scrollTop();
        var height = $(document).height() - $(window).height();
        var progress = pathLength - (scroll * pathLength) / height;
        progressPath.style.strokeDashoffset = progress;
      };
      updateProgress();
      $(window).scroll(updateProgress);
      var offset = 50;
      var duration = 1500;
      $(window).on("scroll", function () {
        if ($(this).scrollTop() > offset) {
          $(".progress-wrap").addClass("active-progress");
        } else {
          $(".progress-wrap").removeClass("active-progress");
        }
      });
      $(".progress-wrap").on("click", function (event) {
        event.preventDefault();
        $("html, body").animate(
          {
            scrollTop: 0,
          },
          duration
        );
        return false;
      });

      if (initialScroll >= 50) {
        $(".progress-wrap").addClass("active-progress");
      }
    }

    /**
     * ======================================
     * 05. add active class to the current link
     * ======================================
     */
    function dynamicCurrentMenuClass(selector) {
      let FileName = window.location.href.split("/").reverse()[0];

      selector.find("li").removeClass("active");
      selector
        .find(".navbar__dropdown-label")
        .removeClass("navbar__item-active");

      selector.find("li").each(function () {
        let anchor = $(this).find("a");
        if ($(anchor).attr("href") === FileName) {
          $(this).addClass("active");
        }
      });

      const activeDropdownItem = selector.find(".navbar__sub-menu .active");
      if (activeDropdownItem.length) {
        activeDropdownItem.parents("li").addClass("active");
      }

      selector.find("li").each(function () {
        if ($(this).find(".active").length) {
          $(this).addClass("active");
        }
      });

      if (FileName === "") {
        selector.find('li:has(a[href="index.html"])').addClass("active");
      }
    }
    if ($("header").length) {
      dynamicCurrentMenuClass($("header"));
    }

    /**
     * ======================================
     * 06. mobile menu
     * ======================================
     */
    if ($(".mobile-menu").length > 0) {
      var mobileMenuContent = $(".navbar__menu").html();
      $(".mobile-menu__list").append(mobileMenuContent);

      $(".mobile-menu .navbar__dropdown-label").on("click", function () {
        $(this).parent().siblings().find(".navbar__sub-menu").slideUp(500);
        $(this)
          .parent()
          .siblings()
          .find(".navbar__dropdown-label")
          .removeClass("navbar__item-active");
        $(this).siblings(".navbar__sub-menu").slideToggle(500);
        $(this).toggleClass("navbar__item-active");
      });
    }

    $(".open-offcanvas-nav").on("click", function () {
      $(this).addClass("open-offcanvas-nav-active");
      $(".mobile-menu__backdrop").addClass("mobile-menu__backdrop-active");
      $(".nav-fade").each(function (i) {
        $(this).css("animation-delay", 0.25 * 1 * i + "s");
      });

      $(".mobile-menu").addClass("show-menu");
      $(".mobile-menu__wrapper").removeClass("nav-fade-active");
    });

    $(".close-mobile-menu, .mobile-menu__backdrop").on("click", function () {
      $(".open-offcanvas-nav").removeClass("open-offcanvas-nav-active");
      $(".mobile-menu").removeClass("show-menu");
      $(".mobile-menu__backdrop").removeClass("mobile-menu__backdrop-active");
      $(".mobile-menu__wrapper").addClass("nav-fade-active");
      $(".mobile-menu .navbar__dropdown-label").removeClass(
        "navbar__item-active"
      );
      $(".mobile-menu .navbar__sub-menu").slideUp(0);
    });

    $(".navbar__item.navbar__item--has-children > a").on("click", function (e) {
      e.preventDefault();
    });

    $(window).on("resize", function () {
      $("body").removeClass("body-active");

      // mobile menu
      $(".mobile-menu").removeClass("show-menu");
      $(".mobile-menu__backdrop").removeClass("mobile-menu__backdrop-active");
      $(".mobile-menu__wrapper").addClass("nav-fade-active");
      $(".mobile-menu .navbar__dropdown-label").removeClass(
        "navbar__item-active"
      );
      $(".mobile-menu .navbar__sub-menu").slideUp(0);
      $(".open-offcanvas-nav").removeClass("open-offcanvas-nav-active");
    });

    /**
     * ======================================
     * 07. fixed header on scroll
     * ======================================
     */
    $(window).on("scroll", function () {
      var scroll = $(window).scrollTop();
      if (scroll < 100) {
        $(".main-header").removeClass("sticky-header");
      } else {
        $(".main-header").addClass("sticky-header");
      }
    });

    if (initialScroll >= 100) {
      $(".primary-navbar").addClass("sticky-header");
    }

    /**
     * ======================================
     * 08. banner one slider
     * ======================================
     */
    var bannerOne = new Swiper(".banner__slider", {
      loop: true,
      speed: 2000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 0,
      effect: "fade",
      fadeEffect: {
        crossFade: true,
      },
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-banner",
        prevEl: ".prev-banner",
      },
    });

    /**
     * ======================================
     * 09. banner two slider
     * ======================================
     */
    var bannerTwo = new Swiper(".banner-two-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 0,
      effect: "fade",
      fadeEffect: {
        crossFade: true,
      },
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });

    var bannerTwoThumb = new Swiper(".banner-two-slider-thumb", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 0,
      effect: "fade",
      fadeEffect: {
        crossFade: true,
      },
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });

    function updateNavigationButtons() {
      var prevButtonImg = document.querySelector(".prev-area img");
      var nextButtonImg = document.querySelector(".next-area img");

      var activeIndex = bannerTwoThumb.activeIndex;
      var totalSlides = bannerTwoThumb.slides.length;

      var prevIndex = (activeIndex - 1 + totalSlides) % totalSlides;
      var nextIndex = (activeIndex + 1) % totalSlides;

      var prevSlide = bannerTwoThumb.slides[prevIndex];
      var nextSlide = bannerTwoThumb.slides[nextIndex];

      var prevImage = prevSlide.querySelector("img").src;
      var nextImage = nextSlide.querySelector("img").src;

      prevButtonImg.src = prevImage;
      nextButtonImg.src = nextImage;
    }

    bannerTwoThumb.on("slideChange", function () {
      updateNavigationButtons();
    });

    /**
     * ======================================
     * 10. banner four video
     * ======================================
     */
    $(".video-four, .video-text").on("click", function () {
      $(".video-text").toggleClass("active");
      $(".video-wrapper").toggleClass("mask-open");
      if ($(".video-text").hasClass("active")) {
        $(".toggle-text").html("Close");
      } else {
        $(".toggle-text").html("Watch");
      }
    });

    $(".video-toggle").on("click", function () {
      $(this).toggleClass("active");
      if ($(this).hasClass("active")) {
        $(this).html(
          "Close Video <span class='material-symbols-outlined'>close</span>"
        );
        $(".video-m").addClass("video-m-active");
      } else {
        $(this).html(
          "View Video <span class='material-symbols-outlined'>add</span>"
        );
        $(".video-m").removeClass("video-m-active");
      }
    });

    /**
     * ======================================
     * 11. search tab
     * ======================================
     */

    $(".search-tab-item").hide();
    $(".search-tab-item:first").show();

    $(".search-tab-btn").on("click", function () {
      $(".search-tab-btn").removeClass("active");
      $(this).addClass("active");
      $(".search-tab-item").hide();
      var target = $(this).data("target");
      $(target).fadeIn(500);
      return false;
    });

    /**
     * ======================================
     * 12. video popup
     * ======================================
     */
    if (document.querySelector(".open-video-popup") !== null) {
      $(".open-video-popup").magnificPopup({
        disableOn: 768,
        type: "iframe",
        mainClass: "mfp-fade",
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false,
      });
    }

    /**
     * ======================================
     * 13. nice select
     * ======================================
     */
    $("select").niceSelect();

    /**
     * ======================================
     * 14. property slider
     * ======================================
     */
    var propertiesSlider = new Swiper(".properties-slider", {
      loop: false,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      grid: {
        rows: 1,
        fill: "row",
      },
      spaceBetween: 30,
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      pagination: {
        el: ".properties-pagination",
        clickable: true,
      },
      breakpoints: {
        768: {
          slidesPerView: 2,
          grid: {
            rows: 1,
          },
        },
        992: {
          slidesPerView: 2,
          slidesPerGroup: 2,
          grid: {
            rows: 2,
          },
        },
        1200: {
          slidesPerView: 3,
          slidesPerGroup: 2,
          grid: {
            rows: 2,
          },
        },
      },
    });

    /**
     * ======================================
     * 15. odometer counter
     * ======================================
     */
    $(".odometer").each(function () {
      $(this).isInViewport(function (status) {
        if (status === "entered") {
          for (
            var i = 0;
            i < document.querySelectorAll(".odometer").length;
            i++
          ) {
            var el = document.querySelectorAll(".odometer")[i];
            el.innerHTML = el.getAttribute("data-odometer-final");
          }
        }
      });
    });

    /**
     * ======================================
     * 16. testimonial slider
     * ======================================
     */
    var testimonialSlider = new Swiper(".testimonial-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-testimonial",
        prevEl: ".prev-testimonial",
      },
    });

    var $arrowPrev = $(".prev-testimonial");

    testimonialSlider.on("slideChange", function () {
      var realIndex = testimonialSlider.realIndex;
      if (realIndex == 0) {
        $arrowPrev.removeClass("active");
      } else {
        $arrowPrev.addClass("active");
      }
    });

    /**
     * ======================================
     * 17. banner tab
     * ======================================
     */

    $(".banner-tab-item").hide();
    $(".banner-tab-item:first").show();

    $(".banner-tab-btn").on("click", function () {
      $(".banner-tab-btn").removeClass("active");
      $(this).addClass("active");
      $(".banner-tab-item").hide();
      var target = $(this).data("target");
      $(target).fadeIn(500);
      return false;
    });

    /**
     * ======================================
     * 18. testimonial three slider
     * ======================================
     */
    var testimonialthreeSlider = new Swiper(".testimonial-three-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-testimonial-t",
        prevEl: ".prev-testimonial-t",
      },
    });

    var $arrowPrevFour = $(".prev-testimonial-t");

    testimonialthreeSlider.on("slideChange", function () {
      var realIndex = testimonialthreeSlider.realIndex;
      if (realIndex == 0) {
        $arrowPrevFour.removeClass("active");
      } else {
        $arrowPrevFour.addClass("active");
      }
    });

    /**
     * ======================================
     * 19. team slider
     * ======================================
     */
    var teamTwoSlider = new Swiper(".team-two-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-team-t",
        prevEl: ".prev-team-t",
      },
      breakpoints: {
        768: {
          slidesPerView: 2,
        },
        1200: {
          slidesPerView: 3,
        },
      },
    });

    var $arrowPrevThree = $(".prev-team-t");

    teamTwoSlider.on("slideChange", function () {
      var realIndex = teamTwoSlider.realIndex;
      if (realIndex == 0) {
        $arrowPrevThree.removeClass("active");
      } else {
        $arrowPrevThree.addClass("active");
      }
    });

    /**
     * ======================================
     * 20. property type slider
     * ======================================
     */
    var propertyTypeSlider = new Swiper(".property-type-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 30,
      centeredSlides: true,
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-property",
        prevEl: ".prev-property",
      },
      breakpoints: {
        576: {
          slidesPerView: 2,
        },
        992: {
          slidesPerView: 3,
        },
        1200: {
          slidesPerView: 5,
        },
      },
    });

    var $propertyArrowPrev = $(".prev-slide");

    propertyTypeSlider.on("slideChange", function () {
      var realIndex = propertyTypeSlider.realIndex;
      if (realIndex == 0) {
        $propertyArrowPrev.removeClass("active");
      } else {
        $propertyArrowPrev.addClass("active");
      }
    });

    /**
     * ======================================
     * 21. partner slider
     * ======================================
     */
    var partners = new Swiper(".partner-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 24,
      freeMode: true,
      centeredSlides: true,
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      breakpoints: {
        420: {
          slidesPerView: 2,
        },
        576: {
          slidesPerView: 3,
        },
        992: {
          slidesPerView: 5,
        },
      },
    });

    /**
     * ======================================
     * 22. property tab
     * ======================================
     */

    $(".property-tab-item").hide();
    $(".property-tab-item:first").show();

    $(".property-tab-btn").on("click", function () {
      $(".property-tab-btn").removeClass("active");
      $(this).addClass("active");
      $(".property-tab-item").hide();
      var target = $(this).data("target");
      $(target).fadeIn(500);
      return false;
    });

    /**
     * ======================================
     * 23. exclusive tab
     * ======================================
     */

    $(".exclusive-tab-item").hide();
    $(".exclusive-tab-item:first").show();

    $(".exclusive-tab-btn").on("click", function () {
      $(".exclusive-tab-btn").removeClass("active");
      $(this).addClass("active");
      $(".exclusive-tab-item").hide();
      var target = $(this).data("target");
      $(target).fadeIn(500);
      return false;
    });

    /**
     * ======================================
     * 24. area slider
     * ======================================
     */
    var areaSlider = new Swiper(".area-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1.2,
      slidesPerGroup: 1,
      spaceBetween: 0,
      effect: "coverflow",
      coverflowEffect: {
        rotate: 20,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
      },
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      pagination: {
        el: ".area-pagination",
        type: "progressbar",
      },
      navigation: {
        nextEl: ".next-area",
        prevEl: ".prev-area",
      },
    });

    var totalSlide = $(".area-slider .swiper-slide").length;
    var fragmentTotal = $(".image-slider__current .total");
    fragmentTotal.text(totalSlide);

    areaSlider.on("slideChange", function () {
      var fragment = document.querySelector(".image-slider__current .cur");
      var current = areaSlider.realIndex + 1;
      var idx = current < 10 ? "0" + current : current;
      fragment.innerHTML = idx;
    });

    var $arrowPrevarea = $(".prev-area");

    areaSlider.on("slideChange", function () {
      var realIndex = areaSlider.realIndex;
      if (realIndex == 0) {
        $arrowPrevarea.removeClass("active");
      } else {
        $arrowPrevarea.addClass("active");
      }
    });

    /**
     * ======================================
     * 25. exclusive slider
     * ======================================
     */

    var exclusiveSlider = new Swiper(".exclusive-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      effect: "fade",
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-exclusive",
        prevEl: ".prev-exclusive",
      },
    });

    var exclusiveThumbSlider = new Swiper(".exclusive-thumb-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      effect: "fade",
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-exclusive",
        prevEl: ".prev-exclusive",
        control: exclusiveThumbSlider,
      },
    });

    /**
     * ======================================
     * 26. coming soon
     * ======================================
     */
    if ($(".clock-wrapper").length) {
      (function () {
        var now = new Date();
        var hourDeg =
          (now.getHours() / 12) * 360 + (now.getMinutes() / 60) * 30;
        var minuteDeg =
          (now.getMinutes() / 60) * 360 + (now.getSeconds() / 60) * 6;
        var secondDeg = (now.getSeconds() / 60) * 360;

        var stylesDeg = [
          "@-webkit-keyframes rotate-hour{from{transform:rotate(" +
            hourDeg +
            "deg);}to{transform:rotate(" +
            (hourDeg + 360) +
            "deg);}}",
          "@-webkit-keyframes rotate-minute{from{transform:rotate(" +
            minuteDeg +
            "deg);}to{transform:rotate(" +
            (minuteDeg + 360) +
            "deg);}}",
          "@-webkit-keyframes rotate-second{from{transform:rotate(" +
            secondDeg +
            "deg);}to{transform:rotate(" +
            (secondDeg + 360) +
            "deg);}}",
          "@-moz-keyframes rotate-hour{from{transform:rotate(" +
            hourDeg +
            "deg);}to{transform:rotate(" +
            (hourDeg + 360) +
            "deg);}}",
          "@-moz-keyframes rotate-minute{from{transform:rotate(" +
            minuteDeg +
            "deg);}to{transform:rotate(" +
            (minuteDeg + 360) +
            "deg);}}",
          "@-moz-keyframes rotate-second{from{transform:rotate(" +
            secondDeg +
            "deg);}to{transform:rotate(" +
            (secondDeg + 360) +
            "deg);}}",
        ].join("");
        document.getElementById("clock-animations").innerHTML = stylesDeg;
      })();
    }

    /**
     * ======================================
     * 27. countdown
     * ======================================
     */
    var endDate = new Date("2025-07-01T00:00:00").getTime();

    var countdown = setInterval(function () {
      var now = new Date().getTime();

      var distance = endDate - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor(
        (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
      );
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      $(".day").text(days);
      $(".hour").text(hours);
      $(".minute").text(minutes);
      $(".second").text(seconds);

      if (distance < 0) {
        clearInterval(countdown);
        $(".day").text("00");
        $(".hour").text("00");
        $(".minute").text("00");
        $(".second").text("00");
      }
    }, 1000);

    /**
     * ======================================
     * 28. testimonial two slider
     * ======================================
     */
    var testimonialTwoSlider = new Swiper(".testimonial-two-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 60,
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      pagination: {
        el: ".testimonial-two-pagination",
        clickable: true,
      },
      breakpoints: {
        1200: {
          slidesPerView: 2,
        },
      },
    });

    /**
     * ======================================
     * 29. explore two slider
     * ======================================
     */
    var exploreTwoSlider = new Swiper(".explore-two-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 30,
      centeredSlides: true,
      roundLengths: true,
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      navigation: {
        nextEl: ".next-explore",
        prevEl: ".prev-explore",
      },
      breakpoints: {
        768: {
          slidesPerView: 2,
        },
        1200: {
          slidesPerView: 3,
        },
        1400: {
          slidesPerView: 2,
        },
      },
    });

    /**
     * ======================================
     * 30. property three slider
     * ======================================
     */
    var propertyThreeSlider = new Swiper(".property-three-slider", {
      loop: true,
      speed: 1000,
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 30,
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      pagination: {
        el: ".property-three-pagination",
        clickable: true,
      },
      breakpoints: {
        992: {
          slidesPerView: 2,
        },
        1200: {
          slidesPerView: 3,
        },
      },
    });

    /**
     * ======================================
     * 31. footer copyright year
     * ======================================
     */
    if ($("#copyrightYear").length > 0) {
      $("#copyrightYear").text(new Date().getFullYear());
    }

    /**
     * ======================================
     * 32. aos initialization
     * ======================================
     */
    AOS.init();

    /**
     * ======================================
     * 33. register gsap
     * ======================================
     */
    gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

    /**
     * ======================================
     * 34. gsap null config
     * ======================================
     */
    gsap.config({
      nullTargetWarn: false,
    });

    /**
     * ======================================
     * 35. target section with gsap
     * ======================================
     */
    $('a[href^="#"]:not([href="#"])').on("click", function (event) {
      event.preventDefault();

      var target = $(this).attr("href");

      gsap.to(window, {
        scrollTo: {
          y: target,
          offsetY: 100,
        },
        duration: 1,
        ease: "power3.inOut",
      });
    });

    /**
     * ======================================
     * 36. parallax image with gsap
     * ======================================
     */
    var imageParallax = document.querySelectorAll(".parallax-image");
    if (imageParallax.length > 0) {
      $(".parallax-image").each(function () {
        $(this).wrap(
          '<div class="parallax-image-wrap"><div class="parallax-image-inner"></div></div>'
        );
        $(".parallax-image-wrap").css({
          overflow: "hidden",
        });

        var $animImageParallax = $(this);
        var $aipWrap = $animImageParallax.parents(".parallax-image-wrap");
        var $aipInner = $aipWrap.find(".parallax-image-inner");

        let tl_ImageParallax = gsap.timeline({
          scrollTrigger: {
            trigger: $aipWrap,
            start: "top bottom",
            end: "bottom top",
            scrub: true,
            onEnter: () => animImgParallaxRefresh(),
          },
        });
        tl_ImageParallax.to($animImageParallax, {
          yPercent: 100,
          ease: "none",
        });

        function animImgParallaxRefresh() {
          tl_ImageParallax.scrollTrigger.refresh();
        }

        let tl_aipZoomIn = gsap.timeline({
          scrollTrigger: {
            trigger: $aipWrap,
            start: "top 99%",
          },
        });
        tl_aipZoomIn.from($aipInner, {
          duration: 1.5,
          autoAlpha: 0,
          scale: 1.3,
          ease: Power2.easeOut,
          clearProps: "all",
        });
      });
    }

    /**
     * ======================================
     * 37. title animation
     * ======================================
     */

    if ($(".title-animation").length > 0) {
      let char_come = gsap.utils.toArray(".title-animation");
      char_come.forEach((char_come) => {
        let split_char = new SplitText(char_come, {
          type: "chars, words",
          lineThreshold: 0.5,
        });
        const tl2 = gsap.timeline({
          scrollTrigger: {
            trigger: char_come,
            start: "top 90%",
            end: "bottom 60%",
            scrub: false,
            markers: false,
            toggleActions: "play none none none",
          },
        });
        tl2.from(split_char.chars, {
          duration: 0.8,
          x: 40,
          autoAlpha: 0,
          stagger: 0.05,
          ease: "back.out",
        });
      });
    }

    /**
     * ======================================
     * 38. lenis smooth scroll
     * ======================================
     */

    if (device_width > 992) {
      const lenis = new Lenis();

      gsap.ticker.add(function (time) {
        lenis.raf(time * 600);
      });
      gsap.ticker.lagSmoothing(0);

      ScrollTrigger.update();
    }
  });
})(jQuery);

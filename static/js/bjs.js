// var swiper = new Swiper(".books-slider", {
//   loop: true,
//   centeredSlides: true,
//   autoplay: {
//     delay: 3500,
//     disableOnInteraction: false,
//   },
//   breakpoints: {
//     0: {
//       slidesPerView: 1,
//     },
//     768: {
//       slidesPerView: 2,
//     },
//     1024: {
//       slidesPerView: 3,
//     },
//   },
// });

document.addEventListener("DOMContentLoaded", function () {
  var swiper = new Swiper(".books-slider", {
    slidesPerView: 3,
    spaceBetween: 10,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
});

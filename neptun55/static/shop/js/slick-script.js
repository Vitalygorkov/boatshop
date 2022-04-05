$(document).ready(function(){
    $('.slider').slick({
     slidesToShow: 1,
     slidesToScroll: 1,
     arrows: true,
     fade: true,
     asNavFor: '.slider-nav',
     responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        slidesToShow: 1,
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        slidesToShow: 1,
      }
    }
  ]
    });
});

$('.slider-nav').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.slider',
  dots: false,
  centerMode: true,
  arrows: false,
  focusOnSelect: true
});

$('.slider-nav-recommend').slick({
  slidesToShow: 5,
  slidesToScroll: 1,
  infinite: false,
  centerPadding: '60px',
  dots: false,
  centerMode: false,
  adaptiveHeight: true,
  arrows: true,
  focusOnSelect: true,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: false,
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: false,
        slidesToShow: 2
      }
    }
  ]
});




//
//$(document).ready(function(){
//    $('.slider').slick({
//  slidesToShow: 1,
//  slidesToScroll: 1,
//  arrows: false,
//  fade: true,
//  asNavFor: '.slider'
//});
//$('.slider').slick({
//  slidesToShow: 3,
//  slidesToScroll: 1,
//  asNavFor: '.slider',
//  dots: true,
//  centerMode: true,
//  focusOnSelect: true
//});
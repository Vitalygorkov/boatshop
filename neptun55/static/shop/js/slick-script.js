$(document).ready(function(){
    $('.slider').slick({
     slidesToShow: 1,
     slidesToScroll: 1,
     arrows: true,
     fade: true,
     asNavFor: '.slider-nav'
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
  slidesToShow: 3,
  slidesToScroll: 1,
  infinite: false,
  dots: false,
  centerMode: true,
  adaptiveHeight: true,
  arrows: true,
  focusOnSelect: true
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
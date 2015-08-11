/**
 * Created by eray on 8/9/15.
 */

var slider = $("#slider");

slider.owlCarousel({
    navigation : false,
    pagination : false,
    slideSpeed : 300,
    paginationSpeed : 400,
    singleItem:true,
    autoPlay: true
});

$(".slider-right").click(function(){
    slider.trigger('owl.next');
});

$(".slider-left").click(function(){
    slider.trigger('owl.prev');
});

var carousel = $("#carousel");

carousel.owlCarousel({
    navigation : false,
    pagination : false,
    slideSpeed : 300,
    paginationSpeed : 400,
    items : 4
});

$("#carouselRight").click(function(){
    carousel.trigger('owl.next');
});

$("#carouselLeft").click(function(){
    carousel.trigger('owl.prev');
});

var services = $("#hizmetlerCarousel");

services.owlCarousel({
    navigation : false,
    pagination : false,
    slideSpeed : 300,
    paginationSpeed : 400,
    items : 4
});

$("#serviceRight").click(function(){
    services.trigger('owl.next');
});

$("#serviceLeft").click(function(){
    services.trigger('owl.prev');
});
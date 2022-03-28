jQuery("document").ready(function($){

	var nav = $('.tabs__items');

	$(window).scroll(function () {
		if ($(this).scrollTop() > 720) {
			nav.addClass("f-nav");
		} else {
			nav.removeClass("f-nav");
		}
	});

});
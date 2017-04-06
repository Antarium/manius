var main = function() {
	$ (window).scroll (function () {
		if ($ (this).scrollTop () > 300) {
		$ ('#totop').fadeIn();
		} else {
		$ ('#totop').fadeOut();
		}
	});
    $("#totop").click(function(){
        $('html, body').animate({ 
            scrollTop: 0 
        }, 1000);
    });
    $(".arrow-bot").click(function(){
    var scroll_el = $(this).attr('data-target');
        $('html, body').animate({ 
            scrollTop: $(scroll_el).offset().top 
        }, 1000);
    });
}
$(document).ready(main);
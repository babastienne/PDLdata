
jQuery("document").ready(function($){
    
    var nav = $('#nav');
    
    $(window).scroll(function () {
        if ($(this).scrollTop() > 150) {
            nav.addClass("floatablenav");
        } else {
            nav.removeClass("floatablenav");
        }
    });
 
});

jQuery("document").ready(function($){
    
    var nav = $('#ligne');
    
    $(window).scroll(function () {
        if ($(this).scrollTop() > 150) {
            nav.addClass("floatable");
        } else {
            nav.removeClass("floatable");
        }
    });
 
});
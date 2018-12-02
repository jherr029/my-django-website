$(document).ready(function(){
    var $heroContainer = $('.hero');

    $heroContainer.height(window.innerHeight);

    $(window).resize(function() {
        $heroContainer.height(window.innerHeight);
    });

    // var $workFilterLinks = $('.work-filters li'),
    //     $container = $('.work-items');

    // $workFilterLinks.find('a').click(function(){

    //     $workFilterLinks.removeClass('active'),

    //     $container.isotope({
    //         filter: $(this).attr('data-filter'),
    //         itemSelector: '.isotope-item',
    //         animationEngine : "best-available",
    //         masonry: {
    //             columnWidth: '.isotope-item'
    //         }
    //     });

    //     $(this).parent().addClass('active');

    //     return false;
    // });
    
    var $menuIcon = $('.menu-icon'),
        $navigation = $('.navigation'),
        $minNavigation = $('.main-navigation'),
        $navigationLink = $('.main-navigation a');

    $(window).scroll(function() {
        if(window.scrollY > window.outerHeight) {
            $menuIcon.addClass('active');
        } else {
            $menuIcon.removeClass('active');
        }
    });

    $menuIcon.click(function(e) {
        e.preventDefault();

        $navigation.toggleClass('active')
    });

    $minNavigation.singlePageNav({
        filter: ':not(.external)',
        speed: 1000,
        currentClass: 'current',
        easing: 'swing',
        updateHash: false,
        beforeStart: function() {
        },
        onComplete: function() {
            $navigation.removeClass('active');
        }
    });

    var config = {

        easing: 'ease-in',
        reset: false,
        delay: 'always',
        opacity: .2,
        viewFactor: 0.4,
        // mobile: false
    }

    // ScrollReveal().reveal('.introduction')
    // ScrollReveal().reveal('.interest')
    // ScrollReveal().reveal('.projects')
    // ScrollReveal().reveal('.contact')
    // ScrollReveal().reveal('.about')
    // $('footer').footerReveal({ shadow: false, zIndex: -101 });

    window.sr = ScrollReveal( config );
    sr.reveal('.introduction')
    sr.reveal('.interest')
    sr.reveal('.projects')
    sr.reveal('.contact')
    sr.reveal('.about')


});
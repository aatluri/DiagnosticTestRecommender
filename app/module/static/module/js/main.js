$(function() {

    // Select Dropdown
    $('html').on('click', function() {
        $('.select .dropdown').hide();
    });
    $('.select').on('click', function(event) {
        event.stopPropagation();
    });
    $('.select .select-control').on('click', function() {
        $(this).parent().next().toggle();
    })
    $('.select .dropdown li').on('click', function() {
        $(this).parent().toggle();
        var text = $(this).attr('rel');
        $(this).parent().prev().find('div').text(text);
    })

    //SETTING PROPER FORM HEIGHT ONLOAD
    window.addEventListener('load', setFormHeight, true);

    //SETTING PROPER FORM HEIGHT ONRESIZE
    window.addEventListener('resize', setFormHeight, true);
})
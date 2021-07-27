$('body').fadeIn(1050);
$('#contact-link').on('click',()=>{
    $('#myModal').slideDown(2000)
    $('.modal-content').animate({
        "opacity":"1"
    },3500);
})
$('#btn-cont button').on('click',()=>{
    $('#myModal').slideDown(2000)
    $('.modal-content').animate({
        "opacity":"1"
    },3500)
})
$('.close').on('click',()=>{
    $('#myModal').css('display','none');
})
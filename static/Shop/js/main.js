$(document).ready(function () {
    $('.sl').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        dots: true
    });
});

function card_delete(item_id, price, qty) {
    $('.cart-header' + item_id).fadeOut('slow', function(c){
        $('.cart-header' + item_id).remove();
    });
    $.ajax({
        method: 'post',
        dataType: 'json',
        url: "remove/" + item_id + '/'
    });
    var block_price = $('.simpleCart_total');
    current_price = block_price.text();
    new_price = current_price - (price * qty);
    block_price.text(new_price);
    var curQty = $('#simpleCart_quantity');
    curQty.text(curQty.text() - qty);
    $('.total1.summ').text(new_price + ' р.');
    $('.last_price span').text(new_price + ' р.')
}

function addToCart (item_id, price) {
    var csrf = $.cookie('csrftoken');
    var data = "quantity=1&update=True&csrfmiddlewaretoken=" + csrf;
    $.ajax({
        data: data,
        method: 'post',
        dataType: 'json',
        url: '/cart/add/' + item_id + '/'
    });
    var block_price = $('.simpleCart_total');
    current_price = block_price.text();
    new_price = parseInt(current_price) + price;
    block_price.text(new_price);
    var curQty = $('#simpleCart_quantity');
    curQty.text(parseInt(curQty.text()) + 1);
}
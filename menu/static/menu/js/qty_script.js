function disableButtons(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#min-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#plus-qty_${itemId}`).prop('disabled', plusDisabled);
}

var qtyInputs = $('.qty_input');
for (var i = 0; i < qtyInputs.length; i++) {
    var itemId = $(qtyInputs[i]).data('item_id');
    disableButtons(itemId);
}

$('qty_input').change(function() {
    var itemId = $(this).data('item_id');
    disableButtons(itemId);
});
    
$('.plus-qty').click(function(e) {
    e.preventDefault();
    var Input = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(Input).val());
    $(Input).val(currentValue + 1);
    var itemId = $(this).data('item_id');
    disableButtons(itemId);
});


$('.min-qty').click(function(e) {
    e.preventDefault();
    var Input = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(Input).val());
    $(Input).val(currentValue - 1);
    var itemId = $(this).data('item_id');
    disableButtons(itemId);
});
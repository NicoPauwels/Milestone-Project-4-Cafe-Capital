// update quantity on change
$('update-item').click(function(e) {
    var form = $(this).parent().prev().find(".update-form");
    console.log("Click");
    form.submit();
});

// remove item
$('remove-item').click(function(e) {
    var csrfToken = "{{ csrf_tokken }}"
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/tab/remove/${itemId}`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
    .done(function(){
        location.reload();
    });
});
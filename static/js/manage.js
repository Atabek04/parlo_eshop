$( '.js-add-to-wish-list').click(function () {
    let item_id = $(this).data('id');
    let data = {
         'action': 'add_to_wish_list',
         'csrfmiddlewaretoken': $('body').find('[name="csrfmiddlewaretoken"]').val(),
         'good_id': item_id,
         'return_url': location. pathname
     }
    $.ajax({
         type: 'POST',
         url: '/cart/',
         datatype: 'json',
         data: data,
         success: function (){
            alert ("Successfully added");
            location.reload();
    }
    })

    return false;
 })


 $( '.js-add-to-compare-list').click(function () {
    let item_id = $(this).data('id');
    let data = {
         'action': 'add_to_compare_list',
         'csrfmiddlewaretoken': $('body').find('[name="csrfmiddlewaretoken"]').val(),
         'good_id': item_id,
         'return_url': location. pathname
     }
    $.ajax({
         type: 'POST',
         url: '/cart/',
         datatype: 'json',
         data: data,
         success: function (){
            alert ("Successfully added");
            location.reload();
    }
    })

    return false;
 })


 $( '.js-add-to-cart').click(function () {
    let item_id = $(this).data('id');
    let data = {
         'action': 'add_to_cart',
         'csrfmiddlewaretoken': $('body').find('[name="csrfmiddlewaretoken"]').val(),
         'amount':1,
         'good_id': item_id,
         'return_url': location. pathname
     }
    $.ajax({
         type: 'POST',
         url: '/cart/',
         datatype: 'json',
         data: data,
         success: function (){
            alert ("Successfully added");
            location.reload();
    }
    })

    return false;
 })

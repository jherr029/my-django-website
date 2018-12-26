function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    console.log("total", total);
    newElement.find(':input').each(function() {
        if ( $(this).attr('name') != null )
        {
            var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
            console.log(name)
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var conditionRow = $('.form-row:not(:last)');
    conditionRow.find('.btn.add-form-row')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row').addClass('remove-form-row')
    .html('<span class="fas fa-minus fa-xs" aria-hidden="true"></span>');
    return false;
}
function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    console.log('total after deletion', total)
    if (total > 1){
        btn.closest('.form-row').remove();
        var forms = $('.form-row');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    cloneMore('.form-row:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
});

$('.submitBtn').on('click', function() {
    var $this = $(this);
  $this.button('loading');
    setTimeout(function() {
       $this.button('reset');
   }, 8000);
});

// console.log("hi")

// $(function()
// {
//     $(document).on('click', '.add-form-row', function(e)
//     {
//         e.preventDefault();

//         var controlForm = $('.form-control form:first'),
//             currentEntry = $(this).parents('.input-group:first'),
//             newEntry = $(currentEntry.clone()).appendTo(controlForm);
        

//         newEntry.find('input').val('');
//         controlForm.find('.input-group:not(:last) .add-form-row')
//             .removeClass('btn-success').addClass('btn-danger')
//             .removeClass('add-form-row').addClass('remove-form-row')
//             .html('<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>');
//     }).on('click', '.btn-remove', function(e)
//     {
// 		$(this).parents('.entry:first').remove();

// 		e.preventDefault();
// 		return false;
// 	});
// });

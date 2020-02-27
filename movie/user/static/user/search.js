$('#btn-search').click(function () {
   var input = $('#input-search').val();
    $('#search-form').submit();
});

$('#input-search').keyup(function () {
   var input = $('#input-search').val();
    $('#search-form').submit();
});
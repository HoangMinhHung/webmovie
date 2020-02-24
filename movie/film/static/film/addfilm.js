$(document).ready(function() {
  $('.director-select2').select2({
    ajax: {
    url: 'http://127.0.0.1:8000/director/',
    dataType: 'text/html;'
  }
});

});
$(document).ready(function() {
    $('.actor-select2').select2();
});
$(document).ready(function() {
    $('.type-select2').select2();
});
$(document).ready(function() {
    $('.category-select2').select2();
});
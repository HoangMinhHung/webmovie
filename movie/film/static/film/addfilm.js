$(document).ready(function() {
  $('.director-select2').select2();
  $('.actor-select2').select2();
  $('.type-select2').select2();
  $('.category-select2').select2();
  $('#id_director').change(function () {
    console.log($('#id_director').val());
  })

});
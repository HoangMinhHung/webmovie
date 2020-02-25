$(document).ready(function() {
    $('.movie-select2').select2();
    $('#id_movie').change(function () {
        console.log($('#id_movie').val());
    })
});

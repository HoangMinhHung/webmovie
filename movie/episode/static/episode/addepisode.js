$(document).ready(function() {
    // $('.movie-select2').select2();
    // $('#id_movie').change(function () {
    //     console.log($('#id_movie').val());
    // });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    $('#comment_form_submit').click(function () {
        // alert("clicked");
        var form = $('#comment_form');
        console.log(form.attr('data-comment-url'));
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: "POST",
            url: form.attr('data-comment-url'),
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                var comment = data["comment"];
                var cm = JSON.parse(comment)[0];
                // alert(JSON.stringify(cm));
                var fields = cm["fields"];
                var username = data["user_name"];
                var comment_count = $('#comment_section').attr("data-comment-count");
                comment_count++;
                if (comment){
                    $('#comment_section').text(comment_count + " comments");
                    $('<div class="comments" style="padding: 10px;"> <p class="font-weight-bold">' + username +'<span class=" text-muted font-weight-normal"> ' + fields["date"] + '</span> </p>'+ fields["content"] +'</div>').insertAfter('#comment_section');
                    // $().append();
                    $('textarea').val('');
                }
            }
        });
    });

    var pathname = window.location.pathname.split("/");
    // alert(pathname[length]);
    var next_episode = $('.next-episode').attr("href");
    if (next_episode != ""){
        pathname[pathname.length-1] = next_episode;
        $('.next-episode').attr("href", pathname.join("/"));
    }
    else{
        $('.next-episode').click(function (e) {
            e.preventDefault();
        });
    }
});

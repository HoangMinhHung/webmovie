from django.shortcuts import render, get_object_or_404

# Create your views here.
from episode.models import Episode

# from comment.forms import CommentForm


# def episode_detail(request):
#     template_name = 'comment/episode_detail.html'
#     episode = get_object_or_404(Episode, id=1)
#     comments = episode.comments.filter(active=True)[0:2]
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.episode = episode
#             user = request.user
#             new_comment.user = user
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'episode': episode,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})

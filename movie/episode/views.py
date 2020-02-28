from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views import View
from film.models import Movie
from .forms import EpisodeAddForm, CommentForm
import json
# Create your views here.
from .models import Episode


class EpisodeAddView(View):
    def get(self, request):
        form = EpisodeAddForm()
        movie = Movie.objects.all()
        return render(request, "episode/add.html", {"movie": movie, })

    def post(self, request):
        form = EpisodeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        return HttpResponse("khong add dc")


def watch(request, pk1, pk2):
    # episodes = Episode.objects.get(name=pk2)
    # print(episodes)
    episodes = Episode.objects.filter(movie__id=pk1)
    episode = Episode.objects.filter(movie__id=pk1, name=pk2)[0]
    # print(episode)
    comments = episode.comments.filter(active=True).order_by("-date")
    new_comment = None
    # Comment posted
    # if request.method == 'POST':
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         # Create Comment object but don't save to database yet
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.episode = episode
    #         user = request.user
    #         new_comment.user = user
    #         # Save the comment to the database
    #         # new_comment.save()
    # else:
    #     comment_form = CommentForm()
    return render(request, 'episode/episode_watch.html',
                  {"episode": episode, "episodes": episodes, 'comments': comments,
                   'new_comment': new_comment}
                   # 'comment_form': comment_form}
                )


def add_comment(request):
    result = "False"
    # print("why")
    if request.method == "POST":
        episode_id = request.POST["episode_id"]
        # print(episode_id)
        episode = get_object_or_404(Episode, id=episode_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.episode = episode
            new_comment.user = request.user
            new_comment.save()
            result = "True"
            print(new_comment.date)
            comment = serializers.serialize("json", [new_comment])
    return JsonResponse({"comment":comment, "user_name": new_comment.user.username})


'''
def add(request):
    form = EpisodeAddForm()
    if request.method == "POST":
        form = EpisodeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/episode")
    return render(request, 'episode/add.html', {"form": form})

def edit(request, pk):
    episode = EpisodeAddForm.objects.get(pk=pk)
    if request.method == "POST":
        form = EpisodeAddForm(request.POST)
        if form.is_valid():
            episode.name = request.POST.get("name")
            episode.episode_url = request.POST.get("episode_url")
            director.save()
            return HttpResponseRedirect("/episode")
    return render(request, 'episode/edit.html', {"episode": episode})

def list(request):
    episodes = Episode.objects.all()
    return render(request, 'episode/view.html', {"episodes": episodes})

def delete(request, pk):
    episode = Episode.objects.get(pk=pk)
    episode.delete()
    return HttpResponseRedirect("/episode")

def detail(request, pk):
    episode = Episode.objects.get(pk=pk)
    return render(request, 'episode/detail.html', {"episode": episode})

def search(request):
    if request.method == "POST":
        form = request.POST
        # if form.is_valid:
        keyword = form["search"]
        episodes = Episode.objects.filter(name__contains=keyword)
        return render(request, 'episode/view.html', {"episodes": episodes})
'''

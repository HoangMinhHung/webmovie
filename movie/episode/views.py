from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from film.models import Movie
from .forms import EpisodeAddForm

# Create your views here.
class EpisodeAddView(View):
    def get(self, request):
        form = EpisodeAddForm()
        movie = Movie.objects.all()
        return render(request, "episode/add.html", {"movie" : movie,})
    def post(self, request):
        form = EpisodeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        return HttpResponse("khong add dc")

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

from django.db.models import Avg
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Review
from . import forms
from .forms import MovieForm, RatingForm
from director.models import Director
# Create your views here.
from category.models import Category

from type.models import Type

from .models import Movie
from episode.models import Episode


class AddMovie(View):
    def get(self, request):
        a = MovieForm()
        director = Director.objects.all()
        category = Category.objects.all()
        type = Type.objects.all()
        return render(request, "film/add.html", {"director": director, "category": category, "type": type})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin/film/movie")


def index(request):
    movies = Movie.objects.all()
    return render(request, 'film/index.html', {"movies": movies})


def searchMovie(request, keyword):
    movies = Movie.objects.filter(title__icontains=keyword)
    # if movies is None:

    return render(request, '', {'movies': movies})


class RatingMovie(View):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        episodes = Episode.objects.filter(movie__id = pk).order_by("-name")[0:3]
        reviews = Review.objects.filter(movie__id = pk)
        ave = reviews.aggregate(Avg('star')).get("star__avg")
        count = reviews.count()
        if ave is None:
            ave = 0
            count = 0
        # print(ave)
        return render(request, 'film/movie_detail.html', {"movie": movie, "count": count, "rate": round(ave), "episodes": episodes})

    def post(self, request, pk):
        value = int(request.POST['get_star'])
        review = Review()
        if 0 < value <= 5:
            # print(value)
            review.star = value
            review.user = request.user
            review.movie = Movie.objects.get(pk=pk)
            review.save()
            return HttpResponseRedirect("/film/"+str(pk))
        return render(request, 'film/rating.html')


from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from .decorators import is_guest

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


class FilmList(ListView):
    paginate_by = 2
    model = Movie
    template_name = 'film/index.html'

    # def get(self, request):
    #     movies = Movie.objects.all()
    #     paginator = Paginator(movies, 2)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     return render(request, 'film/index.html', {'page_obj': page_obj})


# @login_required
@is_guest
def searchMovie(request, keyword):
    user = request.user
    print(user)
    movies = Movie.objects.filter(title__icontains=keyword)
    # if movies is None:
    return HttpResponse(movies)
    # return render(request, '', {'movies': movies})


class RatingMovie(UserPassesTestMixin, View):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            episodes = Episode.objects.filter(movie__id=pk).order_by("-name")[0:3]
            reviews = Review.objects.filter(movie__id=pk)
            ave = reviews.aggregate(Avg('star')).get("star__avg")
            count = reviews.count()
            if ave is None:
                ave = 0
                count = 0
            # print(ave)
            return render(request, 'film/movie_detail.html',
                          {"movie": movie, "count": count, "rate": round(ave), "episodes": episodes})
        except PermissionDenied:
            return HttpResponseRedirect("/")

    def post(self, request, pk):
        try:
            value = int(request.POST['get_star'])
            review = Review()
            if 0 < value <= 5:
                # print(value)
                review.star = value
                review.user = request.user
                review.movie = Movie.objects.get(pk=pk)
                review.save()
                return HttpResponseRedirect("/film/" + str(pk))
            return render(request, 'film/rating.html')
        except PermissionDenied as ex:
            print(ex.get_permission_denied_message())
            return HttpResponseRedirect("/")

    def test_func(self):
        return self.request.user.role.name == 'admin'

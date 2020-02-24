from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from . import forms
from .forms import MovieForm
from director.models import Director
# Create your views here.
from category.models import Category

from type.models import Type


class RatingMovie(View):
    def get(self, request):
        return render(request, 'film/rating.html')

    def post(self, request):
        value = int(request.POST['get_star'])
        if 0 < value <= 5:
            print(value)
            return HttpResponse("You voted %d star" % (value))
        return render(request, 'film/rating.html')


class AddMovie(View):
    def get(self, request):
        a = MovieForm()
        director = Director.objects.all()
        category = Category.objects.all()
        type = Type.objects.all()
        return render(request, "film/add.html", {"director" : director, "category":category, "type":type})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
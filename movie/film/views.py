from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import MovieForm
from director.models import Director
# Create your views here.


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
        d = Director.objects.all()
        return render(request, "film/add.html", {"d" : d})

    def post(self, request):
        return
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DirectorAddForm
from .models import Director

# Create your views here.


def add(request):
    form = DirectorAddForm()
    if request.method == "POST":
        form = DirectorAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, 'director/add.html', {"form": form})


def edit(request):
    director = Director.objects.get()
    return render(request, 'director/edit.html')


def list(request):
    directors = Director.objects.all()
    return render(request, 'director/view.html', {"directors": directors})


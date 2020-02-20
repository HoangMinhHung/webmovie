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
            return HttpResponseRedirect("/director")
    return render(request, 'director/add.html', {"form": form})


def edit(request, pk):
    director = Director.objects.get(pk=pk)
    if request.method == "POST":
        form = DirectorAddForm(request.POST)
        if form.is_valid():
            director.name = request.POST.get("name")
            director.dob = request.POST.get("dob")
            director.nationality = request.POST.get("nationality")
            director.save()
            return HttpResponseRedirect("/director")
    return render(request, 'director/edit.html', {"director": director})


def list(request):
    directors = Director.objects.all()
    return render(request, 'director/view.html', {"directors": directors})


def delete(request, pk):
    director = Director.objects.get(pk=pk)
    director.delete()
    return HttpResponseRedirect("/director")


def detail(request, pk):
    director = Director.objects.get(pk=pk)
    return render(request, 'director/detail.html', {"director": director})


def search(request):
    directors = Director.objects.filter(name__contains="")


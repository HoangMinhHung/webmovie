from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import TypeAddForm
from .models import Type
from film.models import Movie


def add(request):
    form = TypeAddForm()
    if request.method == "POST":
        form = TypeAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/type")
    return render(request, 'type/add.html', {"form": form})


def edit(request, pk):
    type = Type.objects.get(pk=pk)
    if request.method == "POST":
        form = TypeAddForm(request.POST)
        if form.is_valid():
            type.name = request.POST.get("name")
            type.description = request.POST.get("note")
            type.save()
            return HttpResponseRedirect("/type")
    return render(request, 'type/edit.html', {"type": type})


def list(request, name):
    split_name = " ".join(name.split("-"))
    movies = Movie.objects.filter(type__name=split_name)
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'type/view.html', {'page_obj': page_obj})


def delete(request, pk):
    type = Type.objects.get(pk=pk)
    type.delete()
    return HttpResponseRedirect("/type")


def detail(request, pk):
    type = Type.objects.get(pk=pk)
    return render(request, 'type/detail.html', {"type": type})


def search(request):
    if request.method == "POST":
        form = request.POST
        # if form.is_valid:
        keyword = form["search"]
        types = Type.objects.filter(name__contains=keyword)
        return render(request, 'type/view.html', {"types": types})


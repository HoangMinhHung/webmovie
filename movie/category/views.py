from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import CategoryAddForm
from .models import Category
from film.models import Movie


def add(request):
    form = CategoryAddForm()
    if request.method == "POST":
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/category")
    return render(request, 'category/add.html', {"form": form})


def edit(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            category.name = request.POST.get("name")
            category.description = request.POST.get("description")
            category.save()
            return HttpResponseRedirect("/category")
    return render(request, 'category/edit.html', {"category": category})


def list(request, name):
    split_name = " ".join(name.split("-"))
    movies = Movie.objects.filter(category__name=split_name)
    paginator = Paginator(movies, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'category/view.html', {"page_obj": page_obj})


def delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return HttpResponseRedirect("/category")


def detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category/detail.html', {"category": category})


def search(request):
    if request.method == "POST":
        form = request.POST
        # if form.is_valid:
        keyword = form["search"]
        categories = Category.objects.filter(name__contains=keyword)
        return render(request, 'category/view.html', {"categories": categories})


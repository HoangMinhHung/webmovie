from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import CategoryAddForm
from .models import Category


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


def list(request):
    categories = Category.objects.all()
    return render(request, 'category/view.html', {"categories": categories})


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


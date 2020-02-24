from django.shortcuts import render


# Create your views here.
def add(request):
    render(request, 'comment/add.html')

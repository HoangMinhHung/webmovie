from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views import View
from film.models import Movie
import json
from django.http import HttpResponse

# Create your views here.


def autocompleteModel(request):
    if request.is_ajax():
        keyword = request.GET['term']
        movies = Movie.objects.filter(title__icontains=keyword)
        results = []
        print(keyword)
        for r in movies:
            results.extend([r.title, r.movie_url])
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def home(request):
    return render(request, 'user/base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form,}
    return render(request, 'user/profile.html', context)


class Search(View):
    def get(self, request):
        keyword = request.GET['keyword']
        movies = Movie.objects.filter(title__icontains=keyword)
        return render(request, 'user/base.html', {'movies': movies, 'keyword': keyword}, )

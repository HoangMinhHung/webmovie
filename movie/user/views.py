from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views import View
from film.models import Movie
import json
from django.http import HttpResponse


# Create your views here.
from .models import MovieUser
from .token import account_activation_token


def autocompleteModel(request):
    if request.is_ajax():
        keyword = request.POST.get('txt1')
        movies = Movie.objects.filter(title__icontains=keyword)
        results = []
        for mv in movies:
            dict = {mv.title: mv.id}
            results.append(dict)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def home(request):
    return render(request, 'user/base.html')

def register_confirm(request):
    return render(request, 'user/register_confirm.html')
def register_active_done(request):
    return render(request, 'user/register_active_done.html')
def register_active_fail(request):
    return render(request, 'user/register_active_fail.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            MovieUser = form.save(commit=False)
            MovieUser.is_active = False
            MovieUser.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('user/acc_active_email.html', {
                'user': MovieUser,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(MovieUser.pk)),
                'token': account_activation_token.make_token(MovieUser),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            # return HttpResponse('Please confirm your email address to complete the registration')
            # messages.warning(request, f'Please following the instruction email which has been sent to your email address to complete the registration.')
            return redirect('register_confirm')
            # form.save()
            # messages.success(request, f'Your account has been created! You are now able to log in.')
            # return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MovieUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, MovieUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return redirect('register_active_done')
    else:
        # return HttpResponse('Activation link is invalid!')
        return redirect('register_active_fail')


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
    context = {'u_form': u_form, 'p_form': p_form, }
    return render(request, 'user/profile.html', context)


class Search(View):
    def get(self, request):
        keyword = request.GET['txt1']
        movies = Movie.objects.filter(title__icontains=keyword)
        return render(request, 'user/base.html', {'movies': movies, 'keyword': keyword}, )

    def post(self, request):
        keyword = request.POST['txt1']
        movies = Movie.objects.filter(title__icontains=keyword)
        paginator = Paginator(movies, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'film/index.html', {'page_obj': page_obj})

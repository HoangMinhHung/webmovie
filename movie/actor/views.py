from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ActorForm
from .models import Actor
# Create your views here.


def getall(request):
    actors = Actor.objects.all()
    return render(request, 'actor/view_actor.html', {'actors': actors})


class AddActor(View):
    def get(self, request):
        a = ActorForm()
        return render(request, "actor/add_actor.html", {'a': a})

    def post(self, request):
        g = ActorForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("them thanh cong")
        else:
            return HttpResponse("them that bai")


class ViewActor(View):
    def get(self, request, actor_id):
        actors = Actor.objects.get(pk=actor_id)
        return render(request, 'actor/view_actor.html', {'actors': actors})


class SearchActor(View):
    def get(self, request, keyword):
        try:
            list_actor = Actor.objects.filter(name__contains=keyword)
            return render(request, 'actor/search.html', {'actors': list_actor})
        except MultipleObjectsReturned as e:
            print(e)


class EditActor(View):
    def get(self, request, actor_id):
        actor = Actor.objects.get(pk=actor_id)
        return render(request, 'actor/edit_actor.html', {"actor": actor})

    def post(self, request, actor_id):
        actor = Actor.objects.get(pk=actor_id)
        if actor.is_valid():
            form = ActorForm(request.POST)
            if form.is_valid():
                actor.name = form['name']
                actor.dob = form['dob']
                actor.nationality = form['nationality']
                actor.save()
                return HttpResponse("Ban da sua thanh cong")
        return HttpResponse("Ban da sua that bai")


class RemoveActor(View):
    def get(self, request, actor_id):
        b = Actor.objects.filter(pk=actor_id).delete()
        if b[0] != 0:
            return HttpResponse("Delete ok")
        return HttpResponse("Delete fail")




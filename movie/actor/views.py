from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ActorForm
from .models import Actor
# Create your views here.


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
        actor = Actor.objects.get(pk=actor_id)
        return render(request, 'actor/view_actor.html', {'a': actor})


class SearchActor(View):
    def get(self, request, keyword):
        try:
            list_actor = Actor.objects.filter(name__contains=keyword)
            return render(request, 'actor/search.html', {'actors': list_actor})
        except MultipleObjectsReturned as e:
            print(e)



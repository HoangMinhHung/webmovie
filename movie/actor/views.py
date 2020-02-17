from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ActorForm
# Create your views here.


class ActorView(View):
    def get(self, request):
        a = ActorForm()
        return render(request, "actor/actor_view.html", {'a': a})

    def post(self, request):
        g = ActorForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("them thanh cong")
        else:
            return HttpResponse("them that bai")



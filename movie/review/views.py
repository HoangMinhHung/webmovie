from django.shortcuts import render
from django.views import View
# Create your views here.


class RatingMovie(View):
    def get(self, request):
        return render(request, 'review/rating.html')
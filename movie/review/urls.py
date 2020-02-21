from django.urls import path
from .views import RatingMovie
from .models import Review

urlpatterns = [
    path('/', RatingMovie.as_view(), name='rating'),
]
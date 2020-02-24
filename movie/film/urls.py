from django.urls import path
from .views import RatingMovie

urlpatterns = [
    path('rating/', RatingMovie.as_view(), name='rating'),
]
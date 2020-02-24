from django.urls import path
from .views import RatingMovie, AddMovie

app_name = "film"
urlpatterns = [
    path('rating/', RatingMovie.as_view(), name='rating'),
    path('add/', AddMovie.as_view(), name='add'),
]
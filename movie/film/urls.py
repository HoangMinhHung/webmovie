from django.urls import path
from .views import RatingMovie, AddMovie
from . import views
app_name = "film"
urlpatterns = [
    path('rating/', RatingMovie.as_view(), name='rating'),
    path('add/', AddMovie.as_view(), name='add'),
    path('', views.index, name='index'),
]
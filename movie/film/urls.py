from django.urls import path
from .views import RatingMovie, AddMovie
from . import views as film_views
from episode import views as episode_views
app_name = "film"
urlpatterns = [
    path('', film_views.index, name='index'),
    path('<int:pk>', RatingMovie.as_view(), name='detail'),
    path('<int:pk1>/episode/<int:pk2>', episode_views.watch, name='watch'),
]
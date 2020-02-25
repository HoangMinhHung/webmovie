from django.urls import path
from .views import RatingMovie, AddMovie
from . import views
app_name = "film"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', RatingMovie.as_view(), name='detail'),
]
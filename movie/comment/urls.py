from django.urls import path

from movie.comment import views

urlpatterns = [
    path('', views.add, name='add'),
]
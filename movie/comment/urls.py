from django.urls import path

from comment import views

urlpatterns = [
    path('', views.episode_detail, name='episode_detail'),
]
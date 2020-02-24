from django.urls import path

from comment import views

urlpatterns = [
    path('', views.add, name='add'),
]
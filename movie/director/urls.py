from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.list, name='view'),
    path('edit/', views.edit, name='edit'),
]
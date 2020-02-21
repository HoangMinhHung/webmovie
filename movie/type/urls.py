from django.urls import path
from . import views

urlpatterns=[
    path('', views.list, name='type'),
    path("edit/<int:pk>", views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
]
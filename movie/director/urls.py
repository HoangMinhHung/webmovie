from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.list, name='view'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]

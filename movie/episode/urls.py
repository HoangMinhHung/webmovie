from django.urls import path, include
from . import views
from .views import EpisodeAddView

urlpatterns = [
    path('add/', EpisodeAddView.as_view(), name='add'),
    path('', views.watch, name='watch'),
    path('add_comment/', views.add_comment, name='add_comment'),
    # path('edit/<int:pk>', views.edit, name='edit'),
    # path('delete/<int:pk>', views.delete, name='delete'),
    # path('<int:pk>', views.detail, name='detail'),
    # path('search/', views.search, name='search'),
]

from django.urls import path
from .views import Search
from . import views
urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    path('ajax_calls/search/', views.autocompleteModel, name='auto_search'),
]
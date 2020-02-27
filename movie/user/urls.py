from django.urls import path
from .views import Search
<<<<<<< HEAD
urlpatterns = [
    path('search/', Search.as_view(), name='search'),
=======
from . import views
urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    path('ajax_calls/search/', views.autocompleteModel, name='auto_search'),
>>>>>>> b6278122995ff4ddccd574bf7b77ef155aabf88d
]
from django.conf.urls import url
from django.urls import path
from .views import Search
from . import views

urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    path('ajax_calls/search/', views.autocompleteModel, name='auto_search'),

    url(r'^$', views.home, name='home'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]

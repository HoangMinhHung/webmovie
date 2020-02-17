from django.urls import path
from .views import ActorView

app_name = "actor"
urlpatterns = [
    path('view/', ActorView.as_view(), name="view"),
]

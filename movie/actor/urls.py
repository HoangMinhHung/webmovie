from django.urls import path
from .views import AddActor, ViewActor, SearchActor

app_name = "actor"
urlpatterns = [
    path('add/', AddActor.as_view(), name="add"),
    path('view/a<int:actor_id>', ViewActor.as_view(), name="view"),
    path('search/<str:keyword>', SearchActor.as_view(), name="search"),
]

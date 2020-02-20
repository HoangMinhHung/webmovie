from django.urls import path
from .views import AddActor, ViewActor, SearchActor, EditActor, RemoveActor
from . import views
app_name = "actor"
urlpatterns = [
    path('add/', AddActor.as_view(), name="add"),
    path('view/a<int:actor_id>', ViewActor.as_view(), name="view"),
    path('view/all', views.getall, name="view_all"),
    path('search/<str:keyword>', SearchActor.as_view(), name="search"),
    path('edit/<int:actor_id>', EditActor.as_view(), name="edit"),
    path('remove/<int:actor_id>', RemoveActor.as_view(), name="remove"),
]

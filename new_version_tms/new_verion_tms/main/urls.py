from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("planned_loads", views.planned_loads)
]
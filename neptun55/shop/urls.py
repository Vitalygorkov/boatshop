from django.urls import path

from . import views

urlpatterns = [
    path("", views.BoatsView.as_view())
]
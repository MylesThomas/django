from django.urls import path

from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index"),
    #path("", views.default, name="default"),
]
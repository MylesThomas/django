from django.urls import path

from . import views # "import the .py file named views, from this current directory."

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view #1"),
]
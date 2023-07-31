from django.urls import path

from . import views # "import the .py file named views, from this current directory."

urlpatterns = [
    path("<str:name>", views.index, name="index"),
]
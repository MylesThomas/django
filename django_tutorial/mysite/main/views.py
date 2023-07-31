from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, name): # change input
    ls = ToDoList.objects.get(name=name) # name=name input
    item = ls.item_set.get(id=1) # get the first value of the set of todolist itmes
    return HttpResponse("<h1>%s</h1><br></br><p>%s<p>" % (ls.name, str(item.text))) # still prints the name of the ToDoList AND item.name

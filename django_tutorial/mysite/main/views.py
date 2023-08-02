from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    # Checking if we are posting or adding the newItem...
    if response.method == "POST":
        print(response.POST)
        # Seeing which of the 2 new buttons we clicked... 
        # (using a dictionary like this: {"save": ["save"], "c1": ["clicked"]})
        # - note: the item will have a blank value for "" if it is not clicked
        if response.POST.get("save"):
            # loop through all items to see if they were clicked
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                    
                item.save()
            
        elif response.POST.get("newItem"):
            # get text from new field
            txt = response.POST.get("new")
            # before adding new item, let's validate the input (cannot use Django's .is_valid)
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
    
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST) # form takes data from the POST
        
        if form.is_valid(): # automatically is created and exists bc we inherit from forms.Form
            n = form.cleaned_data["name"] # accessing cleaned/unencrypted data from the POST
            t = ToDoList(name=n) # create new to do list
            t.save() # save to DataBase
            
        
        return HttpResponseRedirect("/%i" %t.id) # if response is post... do this instead
    
    else:
        form = CreateNewList()
    
    return render(response, "main/create.html", {"form": form})
# Django

## Setup

Install Linux on Windows with WSL

- Turn on developers mode: Settings > Update & Security > For Developers

  - Developer Mode: On > Yes

- Activate Windows Features: Turn Windows features on or off

  - Windows Subsystem for Linux > Check box > OK

- Install Ubuntu Distribution on Windows: Open Command Prompt (Run as Admin)
  - wsl --install -d Ubuntu (this will take awhile - restart your device after)
    - Ubuntu will open. Enter the following for username/password:
      - Enter a new UNIX username: mylesthomas
      - New password: Myle$
        - you will have to type it twice, but then installation is done!
  - bash (May need to restart your machine before running this)
    - you should see something like this: mylesthomas@USERWC-J77S8OF4:/mnt/c/windows/system32$

Create a project folder

- mkdir django
- cd django

Open VSCode in the project directory

- Open a new VSCode > Open folder > django

Init git / Connect to a remote Git Repository

- Create a repo named 'django' on [github](github.com)
- create the following shell script file `setup.sh`:

```bash
#! /bin/sh

#git config --global user.email "mylescgthomas@gmail.com"
#git config --global user.name "mylesthomas"

echo "# django" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/django.git
git push -u origin main
```

- run the shell script:

```sh
cd django (ie. C:\Users\Myles\django)
bash setup.sh
```

Note: I had issues with bash setup.sh, so I ended up using the command line like normal

## Series: Tech With Tim - Django Tutorial

### Setup

Setup project directory

- mkdir django_tutorial
- cd django_tutorial

### Video #1: Setup, Installation and Page Navigation

#### Intro

Django = Full stack web application

- purely Python
- a little bit of HTML
  - rare framework, usually you need to know CSS/PP/etc.
  - really nice if you already know python!

Goal of this video: Setup the project!

- setup project
- understandin how django works
  - manage.py does all of the work
- running on local machine
- server running on local machine

Other video topics:

- databases
- templates
- fully functioning websites
- large project
- everything needed to make an actual website

#### Get started by seting up a Project Directory and Virtual Environment

Get started by seting up a Project Directory and Virtual Environment

- Create/Init the Virtual Environment:

  - cd django_tutorial
  - py -m venv env

Notes:

- The 'env' folder is where your new directory is
- We do not want this to go up to git...

  - follow this [Link](https://github.com/github/gitignore/blob/main/Python.gitignore) to copy/paste the .gitignore file into the django_tutorial directory as `.gitignore`

- Activate the Virtual Environment:

  - where python
  - .\env\Scripts\activate

- Leaving the virtual environment:
  - deactivate

#### Install Django into your Virtual Environment

Confirm you are in virtual env:

- .\env\Scripts\activate
  - You should see (env) before everything in your command prompt...
  - `pip list` should return pip/setuptools

Install Django with pip:

- py -m pip install django
- pip list

Notes:

- if you want to download a specific page, do it like this: py -m pip install "requests==2.18.4"
- best practice: do NOT use >=

#### Optional: Create a requirements.txt file

Instead of manually updating each package everytime, you can declare all dependencies in a Requirements File. For example you could create a `requirements.txt` file containing:

```
Django==4.2.3
```

Create and run the file with these commands: python -m pip install -r requirements.txt

```sh
# python -m pip freeze
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

- make sure to include the -r flag for 'recursive'

Notes:

- I found out which version of django was the newest by googling OR downloading manually and writing it down
- location of this file: root directory ie. C:\Users\Myles\django\django_tutorial

#### Create a new app / Django project

Create a Django project:

```sh
cd django_tutorial
django-admin startproject mysite
```

Note: This creates a new directory 'mysite' (Make sure not to name it numpy or something like that...)

#### Fire up Dev Server on localport:8080

Fire up Dev Server on localport:8080 to test if our app is working:

```sh
cd mysite
python manage.py runserver
```

Notes:

- When pasting the link into Google Chrome, should see a message saying "The install worked successfully! Congratulations!"

  - If port 8080 is blocked, do this to run on another port: python manage.py runserver 5050

- How to stop server from running: Ctrl-c

#### Create our first app, 'main'

```sh
cd django_tutorial
cd mysite
python manage.py startapp main
```

Note: It is VERY important that 'main' is inside of 'mysite'!

#### Update git

Make sure to be inside of django_tutorial before running these lines of code...

```sh
cd ../../../django
git add .
git commit --message "Created requirements.txt and view function #1, mysite"
git push -u origin main
```

#### View Django app

Start by firing up in Google Chrome:

```sh
cd django_tutorial/mysite
python manage.py runserver
```

Go to: mysite/main/views.py:

- This stores the actual view is the application
  - Where the views (a webpage)
    - Code that serves HTTP requests, and then shows things on the website.

#### Creating the function that represents the view:

- start with 1 view for now
- a view in other words: the code that gets run when an HTTP response is made.

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>tech with tim!</h1>") # need this code to be HTML

# This 2nd view could be imported into urls.py for a different webpage:

# def index2(response):
#     return HttpResponse("<h1>tech with tim!</h1>")
```

Next, create a new file inside of this main application, which represents the URLs.

#### Create urls.py

Creating main/urls.py, which the paths to our different webpages:

```sh
from django.urls import path

from . import views # "import the .py file named views, from this current directory."
urlpatterns = [
    path("", views.index, name="index")
]
```

Notes:

- What this does: If we get into the application's homepage ie. /, we serve this HttpResponse.
-
- We still have to link this application `main` to the project of `mysite`...

#### Linking main to mysite

Remember this about the folders:

- django_tutorial: project folder
- mysite/main: application we link to the project
  - a bit confusing, but proceed...

That is why we need to set the url that links to this application! (We can have more than 1 application in 1 project...)

Edit the mysite/mysite/urls.py file:

```py
from django.contrib import admin
from django.urls import path, include # add this in...

urlpatterns = [
    path('admin/', admin.site.urls), # more on this one later...
    path('', include("main.urls")), # if we don't type anything, take me here!

    # What include function does: We take that given path,
    # and anything that would be after it, we send it to the
    #path('home/', include("main.urls")) this would look for a home path...

]

```

What this says:

- "IF: we navigate to this path ie. http://127.0.0.1:8000/ or http://127.0.0.1:8000/sign-up
- "THEN: navigate to this certain path '/' or '/sign-up'

Notes:

- admin: admin dashboard
- '': Take me to main.urls.py
  - main.urls.py takes the path we have been given, takes us to the view function we imported from views.

Save the files, and you will see the results.

#### Creating a 2nd page

This should help show how everything is working!

Head to main.views.py and create a 2nd function, `v1()`:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>tech with tim!</h1>") # need this code to be HTML

def v1(response):
    return HttpResponse("<h1>view 1!</h1>")
```

Remember: The mysite/urls.py decides "What is going to happen ie. what page we direct to when we go to a certain link"

- Right now: All are sent to main.urls (except for admin...)

Edit the code in main/urls.py to account for the 2nd view:

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="view #1"),
]
```

Now, when you connect to the server with /v1, you will see a different screen!

Notes:

- Remember: `mysite/urls.py` is importing from `main.urls.py`, so no need to change both files!!
  - ie. "Whatever path is given, we hand over to main.urls.py"

Finish up by closing down the server with Ctrl-c.

#### Update git

Make sure to open up a command prompt for django (if you do not, it will only edit from inside of your directory, ie. it will not update these notes!)

```sh
git status
git add .
git commit -m "Completed Video #1 or django_tutorial"
git push
```

### Video #2: SQLite3 DataBase Tutorial

#### Intro

Database Topics:

- setup
- add entries
- retrieve entries

Database of choice: SQLite3

- other choices out there, this one is the best and easiest for beginners!

Notes:

- The information we store is our database and will most likely be more important than the templates/html
  - make the info 1st, display it 2nd!

#### Configuration

Step #1: Configure the mysite/mysite/settings.py file

- Add our new 'main' app to the `INSTALLED_APPS` (this tells Django that we have another application with dependencies, etc.)

Add this code:

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # new
    'main.apps.MainConfig',
]
```

What this means:

- in main, we have main/apps.py
  - there is a class function MainConfig() in this file

Step #2: Migrations, which are Django's way of propogating changes you make to your models into your database Schema.

While in mysite, run the following line of code:

```sh
cd mysite
python manage.py migrate
```

What this does:

- We have updates settings.py, so let's run this to reflect those changes

We are now ready to begin settings up our models.

#### Models

Database Model: Modeling information

- makes it easier to work with data
  - grab data
  - add methods
  - etc.
- contains definitive source info about your data

Let's create our first data model in mysite/models.py:

- class with the name of the model

```py
from django.db import models

# Create your models here.

# #1. creating database object
# (we create a class variable that has name of field AND data type)
class ToDoList(models.Model):
    # define attributes
    # name
    name = models.CharField(max_length=200) # name=name, dtype=string

    # method to get meaningful text (useful for prints)
    def __str__(self):
        return self.name

# 2. item for to do lsit
# (a little different since it is related to the todolist object)
class Item(models.Model):
    # ForeignKey: an undefined object for many-to-one relationships
    ### to do list: can only be 1
    ### items in the list: can be infinite!

    # on_delete=models.CASCADE:
    ### "if, we delete todolist
    ### then, delete all items for that to dolist"
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    # text: character field
    text = models.CharField(max_length=300) # note: always complete max_length arg

    # complete: boolean field (have we finished making this item?)
    complete = models.BooleanField()

    # the meaningful text
    def __str__(self):
        return self.text
```

What is going on here:

- We are creating a model class that inherits from `models.Model`, which is a database model class setup already for Django
- Info about our model:
  1. To do list
  2. Items for the to do list

Now that we have modified our models, we must tell Django that we have done that!

```sh
cd mysite
python manage.py makemigrations main
```

What this does:

- make migrations ie. add something to the staging area
  - app=name

What this does NOT do is actually apply the changes to the app (it essentially is doing version control...) but to apply the change:

```sh
python manage.py migrate
```

Migrations have now been applied!

- if you go into main/migrations/0001_initial.py, you will see changes made
  - useful for a few things;
    - see past changes
    - revert past changes

Now that we have a fully functioming database, let's add some things to it!

#### Adding Objects

Open Python shell to add some things into the database.

```sh
cd mysite
python manage.py shell
```

First, import our models:

```py
# we are not in main directory, so make sure to add main. prior
from main.models import Item, ToDoList
```

Next, create a to do list and add it to the database:

```py
t = ToDoList(name="Tim\'s List")
t.save() # quickly save to DB with this
```

View all of the ToDoList's in the DataBase:

```py
ToDoList.objects.all() # .all() returns a QuerySet, ie. an array of all objects
```

Look at the first item in the to do list:

```py
ToDoList.objects.get(id=1) # objects are added incrementing, and starts at 1 (instead of 0)
# note: if we did not add __str__ method, this would return an ugly memory address!

# another way to get this item: ()
ToDoList.objects.get(name="Tim's List")

# this way will not work: (id=2 has not been created yet, nor has Myles's list)
ToDoList.objects.get(id=2)
ToDoList.objects.get(name="Myles's List")
```

Next, let's create an Item for our first to do list!

#### Creating Items

```py
# viewing items (there will be an empty query set, as we did not add anything yet)
# note: because we added relationship between item and todolist, there is a set of items for each to do list
t.item_set.all() # empty <QuerySet[]>

# Adding the items to the to do list:
# - we 'create' a new item
t.item_set.create(text="Go to the mall", complete=False)

# looking at the new item
t.item_set.all() # <QuerySet [<Item: Go to the mall>]>
t.item_set.get(id=1) # <Item: Go to the mall>
t.item_set.get(id=2) # error
```

Now, in the future, instead of using command line, we will probably set it up in our web browser.

Let's practice this by doing the following:

- remove v1 from `` since that was just for an example
- add functionality so that if you type in a path /, you will be able to see that number on your screen

Cleaning up `main/views.py` ...

```py
def index(response, id):
    return HttpResponse("<h1>%s</h1>" % id) # need this code to be HTML

# def v1(response):
    # return HttpResponse("<h1>view 1!</h1>")
```

Next, do the following to `main/urls.py`:

- remove v1 code
- <int: id>: Look for some int in the path
  - if found: pass that id to views.index

```py
urlpatterns = [
    path("<int:id>", views.index, name="index"),
    # path("v1/", views.v1, name="view #1"),
]
```

Save + Test this out with the following code:

```sh
cd mysite
python manage.py runserver
```

If you go into your browser, you will see the following with the following urls:

- http://127.0.0.1:8000/1 gives a 1
- http://127.0.0.1:8000/99999 gives a 99999
- http://127.0.0.1:8000 gives an error (we got rid of that functionality...)

That was nice practice, but let's implement this so that we are viewing data from our database:

Edit `main/views.py` once again:

- imports
- get the to do list (for the correct id)
- return the name of that to do list object

```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item # import objects from .models
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id) # get the to do list for that id...
    return HttpResponse("<h1>%s</h1>" % ls.name) # print the name of the ToDoList
```

When you save and the server refreshes, you will get the following for each:

- http://127.0.0.1:8000/1: Tim's List
- http://127.0.0.1:8000/2: error (does not exist yet)

Let's try this one more time but with the name attribute instead of id!

Edit `main/views.py` once again:

```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, name): # change input
    ls = ToDoList.objects.get(name=name) # name=name input
    item = ls.item_set.get(id=1) # get the first value of the set of todolist itmes
    return HttpResponse("<h1>%s</h1><br></br><p>%s<p>" % (ls.name, str(item.text))) # still prints the name of the ToDoList AND item.name

```

Then, Edit `main/urls.py` to reflect the new string input:

```py
from django.urls import path

from . import views # "import the .py file named views, from this current directory."

urlpatterns = [
    path("<str:name>", views.index, name="index"),
]
```

Try out these urls and see what you get:

- http://127.0.0.1:8000/Tim's%20List: (Tim's List, Go to the mall)
- http://127.0.0.1:8000/2: error

#### Git commit

Ctrl-c to exit the server and run the following code to finish up this section:

```sh
cd ..
cd ..
git status
git add .
git commit -m "Completed Video #2 of django_tutorial
git push
```

### Video #3: Admin Dashboard

Admin Dashboard

- The admin page/dashbaord is a place where you can view valuable information about your site, specifically your database tables and models.

- relates to databases
  - querying
    - get
    - set
    - delete

Let's start by getting a list of items:

- first, open the shell

```sh
cd mysite
python manage.py shell
```

Next, begin with basic querying on conditions:

```py
# imports
from main.models import Item, ToDoList
# get the list of objects
t = ToDoList.objects
# print all of list (currently length=1)
t.all()

# begin querying: using the filter()
# get all objects that start with t
t.filter(name__startswith="Tim") # gets the same set as above
t.filter(name__startswith="Myles Thomas") # get empty QuerySet (does not exist)

# check if an item actually exists...
t.filter(id=1) # still exists
del_object = t.get(id=1) # grab object to delete
del_object.delete() # deletes the object and returns deleted the entire ToDoList
t.all() # empty QuerySet, we deleted the 1 object
```

Let's go ahead and create 2 to do lists that we can work with:

```py
t1 = ToDoList(name="first list")
t1.save()

t2 = ToDoList(name="second list")
t2.save()

quit() # Exit Python interpreter back out to command prmopt after!
```

Now that we have added data, let's check it out in the admin dashboard!

Step #1: Create login account

- Reasoning for this: If you were to have the following code and run it, you would get to an admin dashboard where you don't have a login!

Note: As you proceed, make sure that only root directory ie. mysite/urls.py has the `path("admin/", admin.site.urls),` functionality in urlpatterns

- Typically: You just have to declare it in the root urls.py of the project in order for it to work how it is supposed to

```sh
cd mysite
python manage.py runserver
chrome.exe http://127.0.0.1:8000/admin/
```

Like I mentioned above, you will get here and become stuck, so let's get unstuck:

Create superuser:

```sh
python manage.py createsuperuser
```

After filling in the info, Fire the server up again...

```sh
cd mysite
python manage.py runserver
chrome.exe http://127.0.0.1:8000/admin
```

### How I was able to figure it out:

Fire up the server and type in http://127.0.0.1:8000/admin.

Entry point: `mysite/urls.py`:

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.sites.urls),
    path("", include("main.urls")),
    # Remember: This is importing from main.urls.py, so no need to change this!
    # ie. "Whatever path is given, we hand over to main.urls.py"
]
```

What this says: "try going to http://127.0.0.1:8000/admin/. If you cannot, head to `main/urls.py`, where you may be able to match based on name or id index."

#### What I was doing wrong

Before: http://127.0.0.1:8000/admin

- this was attempting to match based on id=name with name 'admin'

After: http://127.0.0.1:8000/admin/

Yeah...

error message:

DoesNotExist at /admin
ToDoList matching query does not exist.
Request Method: GET
Request URL: http://127.0.0.1:8000/admin
Django Version: 4.2.3
Exception Type: DoesNotExist
Exception Value:
ToDoList matching query does not exist.
Exception Location: C:\Users\Myles\django\django_tutorial\env\Lib\site-packages\django\db\models\query.py, line 637, in get
Raised during: main.views.index
Python Executable: C:\Users\Myles\django\django_tutorial\env\Scripts\python.exe
Python Version: 3.11.3
Python Path:
['C:\\Users\\Myles\\django\\django_tutorial\\mysite',
'C:\\Users\\Myles\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip',
'C:\\Users\\Myles\\AppData\\Local\\Programs\\Python\\Python311\\DLLs',
'C:\\Users\\Myles\\AppData\\Local\\Programs\\Python\\Python311\\Lib',
'C:\\Users\\Myles\\AppData\\Local\\Programs\\Python\\Python311',
'C:\\Users\\Myles\\django\\django_tutorial\\env',
'C:\\Users\\Myles\\django\\django_tutorial\\env\\Lib\\site-packages']

#### Admin Dashboard - Overview

Authentication and Authorization

Groups:

- we will cover this later...

Users: Stores the user we just created

- USERNAME: myles
- EMAIL ADDRESS: mylescgthomas@gmail.com
- PASSWORD: _encrypted_

Where is our database that we have been creating data with, though?

#### Give the dashboard access to our database

By default, 'main' is empty since nothing is registered in `main/admin.py`.

Head to `main/admin.py` and do the following:

- import the model Object
- Register it

```py
from django.contrib import admin
from .models import ToDoList # need to import this

# Register your models here.
admin.site.register(ToDoList) # register this, to see ToDoList on admin/ site!
```

Refresh the admin/ page, and you should now be able to see `To do lists` under Main.

Current Status:

- Main
  - To do lists
    - first list
    - second list

Notes:

- you can go into here and edit/change things, see history/etc.
- Very useful tool to make sure that whatever you are doing, is working properly!

If we wanted to add Item and see it in the admin/, then this is what our code should look like:

```py
from django.contrib import admin
from .models import ToDoList, Item

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
```

Note on current status:

- To do lists: 2 items
- Items: 0 items

#### Git

```sh
git status
git add .
git commit -m "Completed video #3 of django_tutorial"
git push
```

### Video #4: Templates & Custom HTML

Django is really good because you can do dynamic HTML
- easy way to connect backend to frontend
  - why people love django!

Examples we will cover later:
- forms
- sidebar
- hosting with heroku (hopefully free)

#### Creating Templates

What we will do: Create templates that allow us to see our to-do list on the way in a somewhat nice format
- later videos: Bootstrap for custom CSS
- right now: HTML

Creating a Homepage:

Head to `main/urls.py` and add in the following:

```py
from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"), # new homepage
]
```

And in `main.views.py` ...

```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, name): # change input
    ls = ToDoList.objects.get(name=name) # name=name input
    item = ls.item_set.get(id=1) # get the first value of the set of todolist itmes
    return HttpResponse("<h1>%s</h1><br></br><p>%s<p>" % (ls.name, str(item.text))) # still prints the name of the ToDoList AND item.name

def home(response): # note: no variable
    pass
```

Reminder: What we have been doing so far is passing an HTTP response to our views
- putting HTML into the functions
  - not efficient or scalable!!

How to fix:
- write our own HTML files
- load them up + display to the screen

Step #1: Create directory in `main` named `templates`

```sh
cd mysite
cd main
mkdir templates
cd templates
```

Step #2: Create directory in `templates` named `main`

```sh
mkdir main
cd main
```

Note: It is weird having main again, but in django you NEED to have a folder inside with the same name as the application
- if you do not, the templates will not load!

Step #3: Create a new HTML file `templates/main/base.html`
- Why it is named this:

```html
<html>
<head>
    <title>Tim's Website</title>
</head>

<body>
    <p>Base Template</p>
</body>
</html>
```

Note: If your HTML is not autocompleting, check out these 2 references:
- [Stack Overflow Article](https://stackoverflow.com/questions/30696863/vscode-not-auto-completing-html)
- [Pictures Explanation](https://i.stack.imgur.com/RpE7P.png)

#### Extending a Template

Step #4: Create another HTML file `templates/main/home.html`

```html
{% extends 'main/base.html' %}
```

Topic of discussion here: Template Inheritance
- Something very nice about building websites with Django
- Ours is base.html
  - it will be the base layout of ALL of our website
    - example: on Instagram, the bar being up at the top, search bar, icons, etc. is the base at the top

So what we are going to do essentially is the following:
- Create base.html
- In each of the other .html file, inherit base.html with 1 line of code
  - always is there, unless we choose to override with child templates!

Step #5: Render the templates

Remove http response from our `main/views.py` and replace with render for our views.

```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {}) # leave the dictionary blank for now!
```

This is all we need to show the HTML templates!

Run the site to look:

```sh
cd django_tutorial
cd mysite
python manage.py runserver
```

Reminder: Essentially what happens:
- You direct to the "" endpoint because of the "" and views.home imported in the file `main/urls.py`
- When views.home is called, we render "main/home.html"
- This makes its way all the way up to `main/base.html` (since main/home.html is just an extension from it)

Now, let's type in the 1/ endpoint and see what happens:
- The same base template should be showing up.

Note: If not, try the 2/ with this in _

```

```

#### Using Variables

Let's say we want the base template to show all of our to do list items:

```html
<!-- base.html -->
<html>
<head>
    <title>Tim's Website</title>
</head>

<body>
    <p>({name})</p>
</body>
</html>

```

What we did here:
- to do list name: variable `name`
  - the corresponding `name` gets passed through to the .html file via the dict in `main/views.py`

    ```py
    def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {"name": ls.name})
    ```

    We must make sure we do something similar for the home view:
    - Note: This is a simple fix and we will come back to this

    ```py
    def home(response):
    return render(response, "main/home.html", {"name": "temp"})
    ```

Let's go back and talk about some more advanced stuff we can do.

#### Content Blocks

Ideally, our base page should not have information unique to a list on the home page.

We will set up a content block. This can be over-ridden by other templates.

```html
<html>
<head>
    <title>{% block title %}Tim's Site {% endblock %}</title>
</head>

<body>
    <div id="content" name="content">
        
        {% block content %}
        Default value for title (gets rendered if nothing in the file inheriting)
        {% endblock %}
    </div>

</body>
</html>

```

Now what we can do:
- From inside of other templates that extend off of `main/base.html`, we can pick and choose what goes inside of this block.

For example, with home page `main/home.html`:

```html
{% extends 'main/base.html' %}

{% block title %}
Home
{% endblock %}

{% block content %}
<h1>Home Page</h1>
{% endblock %}
```

Next, go into `main/views.py` and remove the variables from the dicts (we no longer need them...)

```py
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})
```

Render the home page via http://127.0.0.1:8000/

What we have done to get Home Page on the screen:
- Take our base
- The content for each page that inherits from this 
  - anything can go inside of this block content
  - you can always create more than 1 block

Next, we learn about how you don't actually want to use `main/base.html` inside of 1 of your views..
- we want to inherit from it, and customize it from each individual view.

#### List Form + Looping

Create another template to view the to do list ie. `templates/main/list.html`:
- displays name of list
- displays items in the list

```html
{% extends 'main/base.html' %}

{% block title %}
View List
{% endblock %}

{% block content %}
    <h1>{{ls.name}}</h1>
    <ul>
        {% for item in ls.item_set.all %}
        <li>{{item.text}}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

What we did:
- in `main/views.py`, we passed in the entire ls variable.
- in `templates/main/list.html`, we used this variable to fill up the template.
  - ls.name is easy
  - for the items, we had to use python code to loop through the items in each list

Notes:
- We do not need brackets for the .all
- You must end for loops

Make the following changes as well to `main/views.py`:

```py
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls}) # changed to list.html AND passed in ls
```

Add items to the list so that we have items to look at with endpoint 2/

```sh
python manage.py shell
```

```py
from main.models import ToDoList
ls = ToDoList.objects.get(id=2)
print(ls)
print(ls.item_set.all())

ls.item_set.create(text="first item", complete=False)
ls.item_set.create(text="second item", complete=False)
ls.item_set.create(text="third item", complete=False)

print(ls.item_set.all())
quit()
```

```sh
python manage.py runserver
```

The list with 3 items is now on the screen with endpoint 2/ !

#### If Statements

Let's only look at the items in a list that have `complete=True`

Edit the file `templates/main/list.html`:

```html
{% extends 'main/base.html' %}

{% block title %}
View List
{% endblock %}

{% block content %}
    <h1>{{ls.name}}</h1>
    <ul>
        {% for item in ls.item_set.all %}
            {% if item.complete == True %}
                <li>{{item.text}}  -  COMPLETE</li>
            {% else %}
                <li>{{item.text}}  -  INCOMPLETE</li>
            
            {% endif %}
        {% endfor %}
    </ul>
{% endblock %}
```

Note: You must use endif OR an else at end of if-statement, just like a for loop.

None of the items will be visible now - Make another item in this list that will be able to be seen.

```sh
python manage.py shell
```

```py
from main.models import ToDoList
ls = ToDoList.objects.get(id=2)
print(ls)
print(ls.item_set.all())

ls.item_set.create(text="fourth item that you cannot see", complete=True)

print(ls.item_set.all())
quit()
```

```sh
python manage.py runserver
```

### Video #5: Simple Forms

#### Intro

This video: Forms
- essential to any website
  - login format
  - create new... form

What we will do: Create a new to do list

Right now: Create a new to do list, without using the command prompt like before!

#### Create a new page

Starting out: Path to the page, creating a new template:

Go into `main/urls.py` and add a 3rd path:

```py
from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"), # new
    
]
```

Fix the import error we just created by going in `main/views.py` and creating that:

```py
def create(response):
    return render(response, "main/create.html", {})
```

Create the .html file you are referencing above:

```html
{% extends 'main/base.html' %}

{% block title %} Create New List {% endblock %}

{% block content %}
Create Page
{% endblock %}
```

Next, we need to create a form that shows up on our page so that you can input data.

#### Create a form

How we will do this using Django's way, which makes this very easy:
- `form` is what makes it so easy

Create `mysite/main/forms.py`:

```py
from django import forms

class CreateNewList(forms.Form): # inherit from Form
    name = forms.CharField(label="Name", max_length=200) # label: what shows up before little box
    check = forms.BooleanField()
```

Now we need to pass this form into our HTML file ie. `main/create.html`.

#### Pass form to HTML

We must edit `main/views.py` so that it does the following:
- import the form
- pass an instance of the form

```py
# new code
from .forms import CreateNewList

def create(response):
    form = CreateNewList() # create new form, which gets passed into the HTML
    return render(response, "main/create.html", {"form": form})
```

Next, pass this form into our HTML file ie. `main/create.html`:

```html
{% extends 'main/base.html' %}

{% block title %} Create New List {% endblock %}

{% block content %}
Create Page
<form method="post" action="/create/">
    {{form}}
    <button type="submit", name="save">Create New</button>
</form>
{% endblock %}
```

Note: The button and whatnot is standard

Let's check it out!

```sh
python manage.py runserver
```

What we see now on development server at http://127.0.0.1:8000/create/:
- title: Create Page
- name: fill in box for name
- check: boolean checkmark
- button: 'Create New' button

These obviously don't look great. We want to add...
- html
- css

Good thing - Django will allow us to do so!

#### Form Layouts

How to look at the form in a different way:

`form.as_table`: What is showing right now

`form.as_p`: Vertically down

`form.as_ul`: Little dots ie. list items

Example with our code that looks much better:

```html
<!-- create.html -->
<form method="post" action="/create/">
    {{form.as_p}}
    <button type="submit", name="save">Create New</button>
</form>
```

Try this now: Hit 'Create New' before you fill everything out - did you notice what happened?
- Nice looking JavaScript comes up

Why?
- Django creates form in HTML for us
  - It would not be like this for us (another advantage of Django)

#### Optional Fields

Right now, if you do not check the box, you will get another JavaScript error.

How to fix:

```py
# forms.py
check = forms.BooleanField(required=False)
```

#### CRSF Verification

Right now, if you click submit, you get the following error:

```
Forbidden (403)
CSRF verification failed. Request aborted.
```

Why? The CSRF token is missing.

How to fix: Put the following in your .html file everytime you create a form!

```html
<!-- create.html -->
<form method="post" action="/create/">
    {% csrf_token %} <!-- new line of code -->
    {{form.as_p}}
    <button type="submit", name="save">Create New</button>
</form>
```

When you submit, there will be no more issues.

Where is this information being sent, though?

#### POST vs GET

When we hit submit, it is all bundled up and sent to the servers.


Now, time to talk about the different between POST/GET requests.
- POST: Sending data / modifications to the server
  - Good for anything that secret ie. a password to needs to be encrypted
    - other people can see it if it is not encrypted

- GET: When you want to grab information from the server
  - All of the infromation gets pasted into the url
    - the url is read

Why do we have both?
- Different security reasons
  - Example: Technically, GET can do everything POST does
  - POST: data is encrypted
    - example: 
  - GET: data goes into the url ie. https://www.google.com/search?q=hey
    - example: bookmark url

In general takeaway: Use POST!

#### POST

When we use the create page window, we use a post request
- encrypts the name
- need to use POST for when we modify the database

We have already set this actually! Look:

```html
<form method="post" action="/create/">
```

What happens when we have post and get requests?
- it gets passed through the view
  - the view knows if it is POST/GET

Notes:
- Default: GET
- Recommended: POST

How to implement this in the code? (we will be doing things different than post)


```py
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
    
    else:
        form = CreateNewList()
    
    return render(response, "main/create.html", {"form": form})
```

What is happening in this code:
- response.POST has all of the info/data in the form
  - it has a dict of all of the ID's etc. and saves them
  - when you passed this to create a new list, you will have passed the values from response.POST
    - ie. name
    - ie. boolean

Updating this code to reflect more of how we would use this later on:

```py
# views.py
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST) # form takes data from the POST
        
        if form.is_valid(): # automatically is created and exists bc we inherit from forms.Form
            n = form.cleaned_data["name"] # accessing cleaned/unencrypted data from the POST
            t = ToDoList(name=n) # create new to do list
            t.save() # save to DataBase
    
    else:
        form = CreateNewList()
    
    return render(response, "main/create.html", {"form": form})
```

After doing this, let's try creating a new ToDoList and see what happens:

```sh
python manage.py runserver
```

name: bingo
checkbox: false

After clicking, even if you cannot tell (page did not change), you did create a new ToDoList!

#### HTTP Response Redirect

Right now, we are simply returning the form with whatever information we passed in it.

Let's now re-direct to that new to do list (so we can see what it looks like!)

```py
# views.py
from django.http import HttpResponse, HttpResponseRedirect

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST) # form takes data from the POST
        
        if form.is_valid(): # automatically is created and exists bc we inherit from forms.Form
            n = form.cleaned_data["name"] # accessing cleaned/unencrypted data from the POST
            t = ToDoList(name=n) # create new to do list
            t.save() # save to DataBase
            
        return HttpResponseRedirect("/%i" %t.id) # if response is post... do this instead
```

Now, instead of staying on `main/create.html`, we will redirect to `t`, which is our new to do list that says "bingo" at the top!

Next video: Custom Forms
Future videos: Bootstrap CSS and more

### Video #6: Custom Forms

Forms that are more dynamic than the ones before!

Goal:
- Allow user to add an item to their ToDoList
- Add check buttons (to see if they are complete, or not)

Starting out, let's delete this code that we no longer need:

```html
<!-- list.html -->
{% if item.complete == True %}
  <li>{{item.text}}</li> <!-- Remove 'COMPLETE' -->
{% else %}
  <li>{{item.text}}</li> <!-- Remove 'INCOMPLETE' -->
```

Next, start setting up a form inside of the HTML file
- Why we need this: To pass information back to our View using a POST request
  - did user click check button?
  - did they want to add to list?

We need to pass that to view with a POST request - this is what the form in `templates/main/list.html` is for!

```html
<!-- list.html -->

{% extends 'main/base.html' %}

{% block title %}
View List
{% endblock %}

{% block content %}
    <h1>{{ls.name}}</h1>

    <form action="post" action="#"> <!-- beginning of new form -->
        <!-- csrf token (necessary for a form) -->
        {% csrf_token %}
        <ul>
            {% for item in ls.item_set.all %}
                {% if item.complete == True %}
                    <!-- About this list item:
                    type: checkbox (straightforward)
                    value: clicked (it is complete and has been clicked)
                    name: id of the item
                    - sets the name equal to the ID of the item ie. id=4
                    - c helps you get the correct button
                    checked: "default to start off as checked"
                    -->
                    <li><input type="checkbox", value="clicked", name="c{{item.id}}" checked>
                        {{item.text}}
                    </li>
                {% else %}
                    <!-- same thing as above, but without the 'checked' at the end! -->
                    <li><input type="checkbox", value="clicked", name="c{{item.id}}">
                        {{item.text}}
                    </li>
                {% endif %}
            {% endfor %}
        </ul>

        <!-- 
        2 new buttons: SAVE and ADD ITEM 
        SAVE: saves changes to checks
        ADD ITEM: adds the item we will get from a text field
        -->
        <button type="submit", name="save", value="save">Save</button>
        <input type="text", name="new">
        <button type="submit", name="newItem", value="newItem">Add Save</button>
        
    </form> <!-- end of new form -->
{% endblock %}

```

What we did here:
- Wrapped most of this in a form
- Created new buttons
  - save
  - add item
- 
- SCRF

#### Saving a form + Saving the check buttons

Next, we must handle this from our views in `main/views.py`:
- the `index()` method

```py

```

What we did here:
- Check if we are using POST or GET
- 

#### Validation

Try it out at http://127.0.0.1:8000/5

Closing Thoughts:
- This is how you make a custom form!
- Shows you how to do pretty much anything in Django...

#### Looking at the actual POST/GET requests

When pressing Add Item button:

<QueryDict: {'csrfmiddlewaretoken': ['u9FrSktUD1eZCo0Mb9eHR8T7QWHnjMP2gzDECksfJJHltRO1Yw3kOFqtZnBDXio0'], 'new': ['first'], 'newItem': ['newItem']}>
[01/Aug/2023 17:54:23] "POST /5 HTTP/1.1" 200 1124
<QueryDict: {'csrfmiddlewaretoken': ['5ec9uZ1YV7xX0LsXCHPBojy3T8757juPREameZ0j1P0jRegcp4EelQ5p2z1lLP3N'], 'new': ['second'], 'newItem': ['newItem']}>
[01/Aug/2023 17:54:26] "POST /5 HTTP/1.1" 200 1392
<QueryDict: {'csrfmiddlewaretoken': ['aTr9azCltzmO6ArniRGEsZZuBTHyj49rWjpmUzBGzhPaX3fC5evhpwwQKkBOXAIp'], 'new': ['third'], 'newItem': ['newItem']}>
[01/Aug/2023 17:54:29] "POST /5 HTTP/1.1" 200 1660

Meaning:
- new: the name of the new item added
- newItem: ['newItem'] (because this button was clicked!)
- everything else: blank

When pressing Save button:

<QueryDict: {'csrfmiddlewaretoken': ['RIP057RN42GsS4io0F2Tp5oHlpqSLVZXD8NdP7Q8aK9OJx6DN2RwmCV3uQk8pryV'], 'c8': ['clicked'], 'save': ['save'], 'new': ['']}>
[01/Aug/2023 17:56:35] "POST /5 HTTP/1.1" 200 2011
<QueryDict: {'csrfmiddlewaretoken': ['x7fk8LPXv1YDTOh4IX4oV3zcEVtCTX8OjxdxSLOiBJrZKh5jvkT1SA6yNmnSxtHM'], 'c8': ['clicked'], 'c9': ['clicked'], 'save': ['save'], 'new': ['']}>
[01/Aug/2023 17:56:36] "POST /5 HTTP/1.1" 200 2362
<QueryDict: {'csrfmiddlewaretoken': ['ExfG4gvh1XpIVsEObKa9Oo6DtrYdFCgFqXdTOguC7FS4MVs3Y7ZMLVDZCSStj8PD'], 'c8': ['clicked'], 'c9': ['clicked'], 'c10': ['clicked'], 'save': ['save'], 'new': ['']}>
[01/Aug/2023 17:56:37] "POST /5 HTTP/1.1" 200 2713

Meaning
- c8: ['clicked']: first is checked
- c9: ['clicked']: second is checked
- c10: ['clicked']: third is checked
- save: ['save']: (because this button was clicked!)
- new: [''] (we added nothing...)
- everything else: blank


Notes:
- If you do not click a button or check an item, it simply won't get passed in the information
- How .get() works: It is 'kinda' a dictionary
  - if the item does not exist, it will return none

### Video #7: How to Add a Sidebar

#### Intro

Today's video: Adding a sidebar and making things look much nicer!

Pages
- home
- view
- create

#### Add a sidebar with HTML

What we do to add Sidebar: work from `main/base.html`
- easy to work with, because adding it here adds it to every page!

```html
<html>
<head>
    <title>{% block title %}Tim's Site {% endblock %}</title>
</head>

<body>
    {% comment %} this is all new {% endcomment %}
    <div class="sidenav">
        <a href="/home">Home</a>
        <a href="/create">Create</a>
        <a href="/2">View</a>
    </div>

    <div id="content", name="content", class="main">
        
        {% block content %}
        Default value for title (gets rendered if nothing in the file inheriting)
        {% endblock %}
    </div>

</body>
</html>

```

What we did here in the body:
- `div`: a way to style many elements at once
  - div #1: sidenav
    - `href`: where link goes when we click on it 
      - added link tags (`<a>`)
        - /home
        - /create
        - /2

  - div #2: main
  
Next, create a .css stylesheet in the head tag to define what the sidenav will look like:

#### CSS Style Tags

```html
<html>
<head>
    <!--
    .sidenav: anything with class=sidenav
    .sidenav a: any <a> tags in class=sidenav (tag within a class)
    .sidenav a: hover: when you hover over any <a> tags in class=sidenav
    
    -->
    <style type="text/css">
        .sidenav {
            height: 100%;
            width:160px;
            position: fixed;
            z-index: 1; 
            top: 0;
            left: 0;
            background-color: #111;
            overflow-x: hidden;
            padding-top: 20px;
        }

        .sidenav a {
            padding: 6px 8px 6px 16px;
            text-decoration: none;
            font-size: 25px;
            color: #818181;
            display: block;
        }

        .sidenav a:hover{
            color: #f1f1f1;
        }

        .main{
            margin-left: 160px;
            padding: 0px 10px;
        }

    </style>

    <title>{% block title %}Tim's Site {% endblock %}</title>
</head>

<body>
    {% comment %} this is all new {% endcomment %}
    <div class="sidenav">
        <a href="/home">Home</a>
        <a href="/create">Create</a>
        <a href="/2">View</a>
    </div>

    <div id="content", name="content", class="main">
        
        {% block content %}
        Default value for title (gets rendered if nothing in the file inheriting)
        {% endblock %}
    </div>

</body>
</html>

```

Note: To move the main content over to the right, while keeping sidebar on left, we used this CSS:

```css
.main{
  margin-left: 160px;
  padding: 0px 10px;
}
```

#### Trying it out

```sh
cd mysite
python manage.py runserver
```

Note: We don't have a home/ page yet, so if you click on that, you will get an error

This is so nice because django having `main/base.html` allows you to make a sidebar in minutes!

### Video #8: How to Add Bootstrap

#### Intro

Head to bootstrap's website and let's go!

[Link to website](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

#### What is Bootstrap

CSS/JavaScript/JQuery Framework
- Built for mobile, expand for desktop after

#### Download CSS

Copy the stylesheet from the link above (Which is server on a content delivery network)
- We don't actually need to download the stylesheet
  - We are pulling the code from online

```html
<html>
<head>
    ...
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>...</title>
</head>

<body>
...
</body>
</html>
```

Note: It should be at the bottom of the headtags, but right before the title!


#### Add Meta Tags + DOCTYPE HTML

Meta Tags: Setup properties for your website
- Define type of characters
- Help with mobile-look

```html
<!doctype html>
<html>
<head>
    ...
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>...</title>
</head>

<body>
...
</body>
</html>
```

Notes:
- Make sure the meta tags are above the link
- Do not forget `<!doctype html>` as the first line of code

#### Add Scripts

Scripts: Used by many of CSS classes
- make things look nicer
- animation / move things around the page

```html
<!doctype html>
<html>
<head>
...
</head>

<body>
...
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

Notes:
- Add at very end of body tag
- They are not REQUIRED but sometimes things will be off if you do not add them.

We are now ready to use Bootstrap!

#### Starting Out - Styling the Base Template

Recommendation: Use Bootstrap Documentation to find the things you like!
- They make it easy for you on there

Adding code for `main/base.html` template:

```html
<div id="content", name="content", class="main">
    <div class="row justify-content-center">
        <div class="col-8">
            <h1 class="mt-2">My Site</h1>
            <hr class="mt-0 mb-4">
            {% block content %}
            {% endblock %}
        </div>
    </div>
</div>
```

Note: I only edited this area around these 3 div's (1 existed already, anyhow)

#### Testing

```sh
cd mysite
python manage.py runserver
```

The base page looks so much nicer already!

#### Styling Other Pages

Styling the Create Page:

```html
<!-- create.html -->
{% extends 'main/base.html' %}

{% block title %} Create New List {% endblock %}

{% block content %}
<h3>Create Page</h3>
<form method="post" action="/create/" class="form-group">
    {% csrf_token %}
    <div class="input-group mb-3">
        <div class="input-group-prepend">
            <button type="submit", name="save", class="btn btn-success">Create New</button>
        </div>
    {{form.name}}
    </div>
</form>
{% endblock %}
```

Notes:
- Prepend: Puts button on left side of input
- Autofill: Comes from javascript
  - Most of the nice stuff from from Django and/or JS


Styling the View Page:

```html
<!-- list.html -->

```

Notes:
- We combined the checkboxes text with prepend
  - Text is added with an input box

- You can edit the items, but it won't actually save to the DataBase.

#### Boostrapping Documentation

If you want to look at components
- navbar
- buttons
- etc.

You can copy whatever you want from here!

### Video #9: User Registration & Sign Up Page

#### Intro

Fortunately: Django does a lot of the hard work
- All we have to do is format a form + a few others things
- Django makes it a lot easier than usual

And this is why people love Django!

#### Create a new application

Current status:
- application: main

Future status:
- application: main
- application: users or register
  - handles logging in and logging out
    - can be copied and pasted between Django projects!

Create the new app:

```sh
cd mysite
python manage.py startapp register
```

You should now see 'register' in the 'mysite' directory.

#### Modify the URLs

Modify the URLs from within the `mysite/mysite/urls.py` file
- Why? We will link to a view that we create in the new app, `register`

Add a new path in `mysite/mysite/urls.py` that directs to a new page in `register`:

```py
# mysite/mysite/urls.py
urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", ), # this is incomplete, we will come back to it...
    path("", include("main.urls")),
]

```

#### Create a Register Function

Now, link it directly to the function that is in register application, ie. `register/views.py`:

```py
# register/views.py
from django.shortcuts import render

# Create your views here.
def register(response):
    return render()
```

Note: We clearly have not finished this function.

Next, in `mysite/urls.py`, import the views.py so we can access everything inside of it, and then finish the line of code that directs to that path:

```py
# mysite/urls.py
from register import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", v.register, name="register"),
    path("", include("main.urls")),
]
```

Now that we have linked these files up, let's make an actual register HTML page.

#### Create a Register HTML File

We begin this process the same as before, with a templates directory inside of `register`:

```sh
cd register
mkdir templates
cd templates
mkdir register # hence the same name as app...
cd register
```

Reminder: You have to make the subdirectory the same name of the app!

Now, create the register.html file:

```sh
echo > register.html
```

We will extend from the base template in the other directory, as you will see in the following code chunk:

```html
<!-- register.html -->
{% extends 'main/base.html' %}

{% block title %}Create an Account{% endblock %}

{% block content %}
{% endblock %}
```

Note: Because we are in a different directory, make sure to specify where it is coming from.

This file can now be rendered and displayed on the screen!

Next, we will add a form to this same file, `register.html`:

```html
<!-- register.html -->
{% extends 'main/base.html' %}

{% block title %}Create an Account{% endblock %}

{% block content %}
    <form method="POST" class="form-group">
        {% csrf_token %}
        {{form}}
        <button type="submit" class="btn btn-success">Register</button>
    </form>
{% endblock %}
```

What is going on here:
- Form is method of POST: To make sure the information to create the account is secure when sending to backend
- Added a button (Django does not automatically insert those for us)

We have made a form - now let's pass the form to a view.

#### Create a form

We need to pass an actual form to the view of `register.html`, we created. 

Django automates the form for logging in and creating a new account
- makes it for you

So, all we need to do is import the built-in Django form, and pass it into our template where we have {{form}}

In `register/views.py`:

```py
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm # used to create a new user

# Create your views here.
def register(response):
    form = UserCreationForm()
    return render(response, "register/register.html", {"form": form})
```

One more step: We need to add the application of 'register' into `mysite/mysite/settings.py`:

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'register.apps.RegisterConfig', # new, comes from mysite/register/apps.py
]
```

#### Run the server

Now, if we run the server and go to this endpoint, we should see a form showing up!

```sh
cd mysite
python manage.py runserver
```

http://127.0.0.1:8000/register/

This form is not styled yet, but we already have a user registration window!

Note:
- If we type anything in here, the register button does nothing right now!
  - Just like making a form before, we need to add functionality to save the form AND create the new user in the database

Let's validate that we can start saving things before we do any styling:

Go into `register/views.py` and add functionality to create a new user:

```py
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm # used to create a new user

# Create your views here.
def register(response):
    if response.method == "POST": # create a new user
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save() # What this does: Saves new user info into the users database
    
    else: # if for some reason we are not getting the post request...
        form = UserCreationForm()
        
    return render(response, "register/register.html", {"form": form})
```

We are not done totally, but should have enough to create a user in the database.

#### Create an account

http://127.0.0.1:8000/register/

username: techwithtim
password: techwithtim123

Notes:
- I got an error...

Using the URLconf defined in mysite.urls, Django tried these URL patterns, in this order:

admin/
register/ [name='register']
<int:id> [name='index']
[name='home']
create/ [name='create']
The current path, register/POST, didn’t match any of these.

What I think this means: The return value of the method register() in `register/views.py` directs you to / render HTML that does not exists in the `mysite/urls.py`.

What the actual error was: I had something wrong in my form ie. `register.html`:

```html
<!-- before (wrong) -->
<form action="POST" class="form-group">

<!-- after (correct) -->
<form method="POST" class="form-group">
```

We have successfully registered a new user now!

Let's check to see if the user is in the Users database: http://127.0.0.1:8000/admin/
- Authentication and Authorization > Users

I only see the original still......

fffffffffffffffff

Next, how to get email/first name/last name, AND redirect to a new page once you create an account!

#### Create register form

Head into `register/views.py` and add this functionality so you head to the home page:

```py
from django.shortcuts import render, redirect # new

...

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save() 

        return redirect("/home") # new
```

Next, add new fields to our form by editing inside of our application:

```sh
cd mysite
cd register
echo > forms.py
```

And in that new file, `register/forms.py`:

```py
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User # changes user model when we save something into this form
        
        fields = ["username", "email", "password1", "password2", ] # in order...
        # fields: lays out where we want the fields to be
        # email would not show up because it is currently not in the parent class!
        # We type them in in the order we want them to appear in the form
```

What we did:
- Import the same things as before
- Inherit from UserCreationForm
  - but then added new fields to it....

- Something that we have not done before: Changing the parent properties of the class
  - create new class `Meta` inside of this class
    - defines the fact that this register form is going to save into the Users database

#### Import register form

Now that we have created this `RegisterForm`, we must import it and use that instead of its parent of UserCreationForm!

In `register/views.py`:

```py
from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST": 
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save() 

        return redirect("/home")
        
    else: 
        form = RegisterForm()
        
    return render(response, "register/register.html", {"form": form})
```

Now, we can reload the page and see what we get!

```sh
cd mysite
python manage.py runserver
```

http://127.0.0.1:8000/register/

It may be messy, but we now have the following (in order):
- username
- email
- password
- password confirmation

Let's make this a little nicer with Bootstrap and Crispy Forms!

#### Install Cripsy Forms

Cripsy Forms: Popular form framework used in Django
- downloadable via pip

```sh
pip install django-crispy-forms
pip list # make sure it is in the virtual env...
```

What it has:
- automatic styling for our forms
- it is easy to use!

Once you have it installed (I have version 2.0), we have a few more steps to take.

#### Add Cripsy Forms to Settings

First, head into `mysite/settings.py` and add crispy forms:

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms", # new
    'main.apps.MainConfig',
    'register.apps.RegisterConfig',
]
```

#### Configure Cripsy Forms

Next, in the same file `mysite/settings.py`, define the CSS framework layout that crispy forms uses:

```py
# bottom line of code under STATIC_URL
CRISPY_TEMPLATE_PACK = "bootstrap4"
```

What this means:
- We are using bootstrap 4
  - default: uses bootstrap 2
  - you can use others too! (we are already using bootstrap4 in the project, so not us)

Now that that work is done, we actually have to use/implement crispy forms!

#### Implement Crispy Forms

Now that they are imported and setup in the project, we have to do the following in `register/register.html` using it:

```html
{% block title %}Create an Account{% endblock %}
{% load crispy_forms_tags %} <!-- new line -->
```

Then, to actually use it, we add `|crispy` after `form` in the HTML of `register/register.html`

```html
{{form|crispy}}
```

What this does:
- it is a filter
  - in a nutshell: modifies the form, adds styling to it

Let's check it out in the server!

```sh
cd mysite
python manage.py runserver
```

http://127.0.0.1:8000/register/

Notes: I am getting an error about "TemplateDoesNotExist at /register/
bootstrap4/uni_form.html
- This is why: [Link to Stackoverflow](https://stackoverflow.com/questions/75495403/django-returns-templatedoesnotexist-when-using-crispy-forms)
  - Remedy: Instead of using bootstrap4 and crispy-forms, you must do the following:
    - Uninstall un-needed package
    - Install needed package
    - Add crispy_bootstrap4 to your list of INSTALLED_APPS.

```sh
# pip uninstall django-crispy-forms (we end up downloading it again...)
pip install crispy-bootstrap4
```

```py
# mysite/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms", # keep as-is
    "crispy_bootstrap4", # this is what matters here.
    'main.apps.MainConfig',
    'register.apps.RegisterConfig',
]
...
CRISPY_TEMPLATE_PACK = "bootstrap4" # keep as-is
```

Now our forms look crispy!
- We could probably add a sidebar, but we can come back to that later...

#### Git

```sh
cd django
git status
git add .
git commit -m "Completed Video #9 of Tim's django_tutorial"
git push -u origin main
git status
```

### Video #10: Login, Logout and User Authentication

Today's video: Logging in and Authenticating Users
- restricting pages to certain users

Next video: Customer user model
- looking at only your own stuff, essentially

#### Django contrib auth

Built in function: django.contrib.auth (it is already in INSTALLED_APPS in `mysite/settings.py`)
- Authenticates users
  - We do hard work of creating new users
  - Django does work of authenticating them

Step #1: Use some pages built by Django
Examples:
- login
- logout
- change password

We can access these, simply by linking them to `mysite/urls.py`:

```py
from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", v.register, name="register"),
    path("", include("main.urls")),
    path("", include("django.contrib.auth.urls")),
]
```

What this will do now:
- it will go to the `urls.py` file/application in the directory of django/contrib/auth
- will confirm/check if we have a valid url
  - ie. any of the built in pages like login/logout

But, if we try to go to these views now, they don't actually exist yet!
- What the views attempt to do is render templates ie. `login.html` and `logout.html`
  - This gets done from a folder we create

#### Login form

Let's create a new folder in `register/templates` named `registration`, and create a new file `login.html`:

```sh
cd register
cd templates
mkdir registration
cd registration
echo login.html > login.html
```

```html
<!-- login.html -->
{% extends 'main/base.html' %}

{% block title %}
Login Here
{% endblock %}

{% load crispy_forms_tags %}

{% block content %}
    <form method="POST" class="form-group">
        {% csrf_token %}
        {{form|crispy}}
        <p>Don't have an account? Create one <a href="/register">here</a></p>
        <button type="submit" class="btn btn-success">Login</button>
    </form>
{% endblock %}
```

Notes:
- Added some p tags for if you don't have an account (then an a tag if you actually don't, and want to create one)

That is it for the login page!

#### Login redirect

Now, let's run the server and see that the login page works:

```sh
cd mysite
python manage.py runserver
```

[Link](http://127.0.0.1:8000/login)

What will happen here: 
- properly log users in
- properly validate

When you try logging in, what happens?
- For me: I am directed to http://127.0.0.1:8000/accounts/profile/, and get an error: 

Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/accounts/profile/
Using the URLconf defined in mysite.urls, Django tried these URL patterns, in this order:

Note: Tim is redirected to the home page ie. http://127.0.0.1:8000, I do not know why ours are different, but we will find out soon enough!
- Tim says it is because of a setting in `mysite/settings.py`
  - He proves this by showing us on the screen himself...

How to fix this and get back to home page?

```py
# settings.py
...

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "/" # NEW
```

What was happening:
- When you try to login, they try to direct you to /accounts/profile
  - This does not exist yet, as we did not make it!
  - We need to change the settings so that this is overcome (for now)

Now when you re-run, you will see that you are directed to the homepage.
- Start: http://127.0.0.1:8000/login/
- End: http://127.0.0.1:8000/


#### User authentication

What is actually going on in the backend when we login?
- 

How to tell if a user is logged in: `user.is_authenticated`
- By default: Django webpages have a `user` attribute
  - stands for current user
  - if no user is signed in, defaults to anon
  - calling user.is_authenticated on anon will return `false`.

Let's illustrate by editing some code from `main/base.html`:

```html
<div id="content", name="content", class="main">
        <div class="row justify-content-center">
            <div class="col-8">
                <h1 class="mt-2">My Site</h1>
                <hr class="mt-0 mb-4">

                {% if user.is_authenticated %}
                    {% block content %}
                    {% endblock %}
                {% else %}
                    <p>Login <a href="/login">Here</a></p>
                {% endif %}
            </div>
        </div>
    </div>
```

Goal here:
- if logged in: show content!
- if NOT logged in: tell the user to login, leave a link for the login page

Now that we have implemented this into our code, let's try it out:

```sh
cd mysite
python manage.py runserver
```

First, logout: http://127.0.0.1:8000/logout/

Next, head to home to (try to) view the block content: http://127.0.0.1:8000/

Note: We are stuck now that we are not logged in, so this is not a final solution. Put your code back to how it was before:

```html
<!-- main/base.html -->
<div id="content", name="content", class="main">
    <div class="row justify-content-center">
        <div class="col-8">
            <h1 class="mt-2">My Site</h1>
            <hr class="mt-0 mb-4">
            {% block content %}
            {% endblock %}
        </div>
    </div>
</div>
```

#### Optional: Change logout redirect

```py
# mysite/settings.py
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/" # NEW
```

If you create a logout template, you can direct it there instead of the home page.

#### Optional: Using response.user in Python Code

```py
# register/views.py
response.user
```

response.user: gives user 
- user authentication status 
- attributes
  - name
  - password
  - email

- can pass into content of the page

### Video #11: User Specific Pages/Access

#### Intro

Tim: Was going to do custom user models, but to do what he wants, you do not need to use those
- they overcomplicated things
- we will do it the original way
  - if you want to do custom user modules, there are other tutorials

Goal of this video: Make specific to do lists for specific users
- When you log in, you see only your things
  - just like facebook, users see custom posts

#### Importing User Model

Starting out, in `main/models.py`, we will add a Foreign Key to ToDoList() called `user`
- now, users will have a ToDoList set
  - you can view all of that user's ToDoList's

```py
from django.db import models
from django.contrib.auth.models import User # NEW

# Create your models here.
class ToDoList(models.Model):
    # related_name: name/way with which you access it in html
    # null: 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # NEW: every to do list we make will be linked to some user
    name = models.CharField(max_length=200) 
    
    def __str__(self):
        return self.name
```

What this code does:
- import User
- make it so that each ToDoList is linked to a user

Notes:
- we first tried settings this up without `related_name=todolist` OR `null=True`, and we got errors
- 

Next, we need to make some migrations so that our database is updated accordingly.

#### Optional: Delete Everything

Notes from Tim: The migrations should be created for you. (automatically)
- If for some reason this does not work, do the following:
  - Delete database file `db.sqlite3`
  - Delete everything in `migrations`, namely `__pycache__`
    - so everything except for `__init__.py`

Note: This is for all of the migrations folders, which for us is 2: (`main/migrations`, `register/migrations`)

If you have further changes to be made to either of your models.py files, do so now as well.
- We already did ours above, so good to go here!

#### Make Migrations

As noted above, when you make edits to your database and models, you must make migrations.

Finish up by doing the following:
- `makemigrations`: for creating new migrations based on the changes you have made to your models
- `migrate`: for applying and unapplying migrations.

```sh
cd mysite
python manage.py makemigrations
python manage.py migrate
```

After doing this, you should see a new db.sqlite3 file appear!

[Stackoverflow Reference](https://stackoverflow.com/questions/42150499/how-do-i-delete-db-sqlite3-in-django-1-9-to-start-from-scratch)


#### Saving ToDoList

Let's change the code in `main/views.py` so that the ToDoLists are saved to a specific user:

```py
# main/views.py
if form.is_valid():
  n = form.cleaned_data["name"]
  t = ToDoList(name=n)
  t.save()
  response.user.todolist.add(t) # this still links back to the id
```

Note: You can still access our to do lists using id of the ToDoList, but we are going to modify this a little bit so you can only access ids/to do lists that are yours:
- Can only 
- Check if ID is in user set, grant permission if yes.

We want to now be able to go to all of our to do lists.

#### Viewing ToDoList

Now, in our HTML file, we had setup a temporary endpoint to send us to ToDoList with id=2 - let's change that in our `main/templates/main/base.html` file:

```html
<!-- old -->
<a href="/2">View</a>

<!-- new -->
<a href="/view">View</a>
```

Now, we are being sent to the correct page with HTML.

We must update our url's in `main/urls.py` to reflect this:

```py
urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
]
```

Next, create the method view() in `main/views.py`
- (Currently as it stands, views.view is going to get an import error as it is linking to nothing).

```py
# main/views.py
def view(response):
    return render(response, "main/view.html", {})
```

Once again, we are linking to something that does not exist yet - create `main/view.html` so that our view can link to a view template:

```sh
cd main
cd templates
cd main
echo > view.html
```

Our view will extend from the base template:

```html
<!-- main/view.html -->
{% extends 'main/base.html' %}

{% block title %}
View
{% endblock %}

{% block content %}
    {% for td in user.todolist.all %}<!--  use .all instead of _set (set is not iterable) -->
        <p><a href="/{{td.id}}">{{td.name}}</a></p>
    {% endfor %}
{% endblock %}

```

What this does:
- Basic title
- For loop through all of the different to do lists (for this user)
  - if: 
  - then: 

In the end, we should see all of our to do lists in a list-type form, with links to the lists.
- Click on the link to access to do lists

Let's try it out!

#### Optional: Create Super User

I deleted everything in one of the optional steps above, so there are no users in /admin, and I will be stuck at the login page again.

Do this to create a super user:

Create superuser:

```sh
python manage.py createsuperuser
```

After filling in the info, Fire the server up again...

```sh
cd mysite
python manage.py runserver
chrome.exe http://127.0.0.1:8000/admin
```

There is this in the database now:
- 0 Groups
- 1 Users
- 0 Items
- 0 To do lists

Excellent!

#### Testing it out

```sh
cd mysite
python manage.py runserver
```

Note: You must be logged in to see any of your to do lists, so let's do that from the start.

Go to login: http://127.0.0.1:8000/login/

Create your first to do list and name it 'l1': http://127.0.0.1:8000/create/
- You will be redirected to http://127.0.0.1:8000/1

Next, 'add item' the following 3 items:
- uno
- dos
- tres

Hit 'save' when you are finished. (This will do nothing, since you did not check off any of the 3 items...)

Create your first to do list and name it 'l2': http://127.0.0.1:8000/create/
- You will be redirected to http://127.0.0.1:8000/2

Next, 'add item' the following 2 items:
- small item
- big item

Check the box so that small item is complete, but big item is not, and press save.

Finally, view your 2 new lists at the view page: http://127.0.0.1:8000/view/

Nice work!

#### Creating Another Account

Let's make another account and create a 3rd to do list and see how this works.

Logout: http://127.0.0.1:8000/logout/
- For fun, you can go to the View page and see that nothing is there now.

Make the new account: http://127.0.0.1:8000/register/
- username: techwithtim
- email: techwithtim@gmail.com
- password: techwithtim123

fffffffffffffffffffffffff

I am seeing now that somewhere my code for adding a new user is flawed.... :(

Login:
- If you don't login and try to create a new list, you will get an error like this:

```
AttributeError at /create/
'AnonymousUser' object has no attribute 'todolist'
```

Create a new page and name it 'Tim's list': http://127.0.0.1:8000/create/

...
tbd

#### Adding Functionality so that you can only view your own To Do Lists

As it stands when you are logged in:
- You do not see other people's to do lists on the view/ page
  - BUT, you can go into the url and type http://127.0.0.1:8000/1/, and you will see the list, even if you did not create that list

Let's change that!

Head over to `main/views.py` and add functionality to block other's from viewing others' lists:

```py
# main/views.py
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    # check if it is in that user's list:
    if ls in response.user.todolist.all():

        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                        
                    item.save()
                
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        
        return render(response, "main/list.html", {"ls": ls})
    
    else:
        # can render error page OR homepage OR their own view page
        return render(response, "main/view.html", {})
```

What we did here:
- Checked if to do list is in user's list
  - if yes: continue
  - if not: deny access
    - 3 options here: send to homepage OR give an error page OR view their own view page
      - I chose to send to that user's own view page

Now, if another user tries to access your list, they will be re-directed away.
- This is not the most secure way in the world, but is a basic example that works good enough for now!

# End of Series

#### Git

```sh
git status
git add .
git commit -m "Completed Tech With Tim's Django Tutorial Course"
git push -u origin main
git status
git log --oneline
```

#### Deactivate Virtual Environment

```sh
deactivate
```

---

## Series: Tech With Tim - Django & React Tutorial

### Setup

Setup project directory

- mkdir django_and_react_tutorial
- cd django_and_react_tutorial

### Video #1: Full Stack Web App With Python & JavaScript

#### Intro

Back end: Python/Django
Front end: JavaScript/React

Project idea: Collaborative Music Playing System

- 1 host: creates a room, controlls the music at the event
- people can then join the room
  - vote to skip song
  - pause/play
    - whatever permissions you grant them!

What this tutorial series is for: Learning a ton

- project
- how frameworks and modules work
  - you will have the skills to do your own after this
- integrate with 3rd party APIs
  - Spotify/Google working on your app!

Note: Not designed for beginners

- used Python and JS before

#### Setup

Download VSCode

- [Download Link](https://code.visualstudio.com/download)

Download Python

- [Download Link](https://www.python.org/)

Download npm/NodeJS

- [Download Link](https://docs.npmjs.com/getting-started)

Install Extensions (Ctrl-Shift-X)

- prettier (makes writing HTML and JavaScript easier)
- python
- django
- es7 react
- javascript (es6)

Note: If you are even un-sure, just download the extension with the most downloads!

Install Django + Django REST Framework

- pip install django djangorestframework

Create for music controller app

- django-admin startproject music_controller

Note: This will make a folder 'music_controller', with another folder with the same name inside of it.

- The 1st folder will have manage.py
  - will talk about this later

Notes:

- The 2nd folder (subdirectory) will have **init**.py, settings.py, and more

  - settings.py: all settings for the projecty

- Django app project folder:
  - project
    - apps within that project (apps are what gets rendered on the screen)

#### Creating App #1 - Handling the API

Change into the correct directory

- cd music_controller
  - We want to be in the first folder so that another app folder is created.
    - 1: music_controller
    - 2: api

Create a new API app

- django-admin startapp api
  - you will now see the 'api' folder. contents:
    - migration: we will talk about this later
    - **init.py**: makes it a python package
    - admin.py
    - apps.py
    - models.py: Database models go here
    - tests.py: Tests for views/models
    - views.py: The code that is actually responsible for rendering our views (ie. api endpoinds)

Remember: music*controller is the directory that has everything inside of it *

- sub-directory music_controller is the project settings, etc.
  - api is an app inside

Add this new app to the project

- Head to music_controller/settings.py and add the following line to INSTALLED_APPS:

```py
INSTALLED_APPS = [
    ...
    'api.apps.ApiConfig', # referencing / adding this app / Class to the project

    'rest_framework' # we are going to need this later so add now...
]
```

Notes:

- api: the name of the app your are configuring
- ApiConfig: a class inside of the file api.apps.py

Optional: View the class inside of the file api.apps.py

- Head to music_controller/api/apps.py and simply view the ApiConfig class:
  - This class was automatically created when we created the app 'api'

#### Create our 1st View

Go inside of api/views.py

- this python file is where we write all of our endpoints
  - examples:
    - / hello
    - / hi
    - any location on the web server!

Create your 1st view

- write the following code:

```py
from django.shortcuts import render # was already here
from django.http import HttpResponse # used later in the video

# Create your views here.
def main(request):
    return HttpResponse("Hello") # this text is what is shown on the webpage when we hit this endpoint
```

What this code does:

- takes in a `request`
- returns a `response`
  - whenever you have a web server, there are incoming requests
    - those requests go to an endpoint...
      - that endpoint will return a response to the center
        - response can be in any of the following:
          - html
          - json

Figure out the url/path to this function (ie. /main)

- create file urls.py inside of api folder
  - urls.py: Going to store all of the local to this app

Check out the main URL

- Head to the music_controller/urls.py file
- Look at the following lines of code:

```py
urlpatterns = [
    path('admin/', admin.site.urls),
]
# 'domain.com/hello'
```

What this does:

- after the slash will get sent to this file
  - this file dispatches the URLs to the correct applications
    - right now code:
      - if: we see a url that looks like /admin/...
      - then: send that admin to site.urls
        - it will take care of what needs to be rendered

Edit the main URL for our new View ()

```py
from django.contrib import admin
from django.urls import path, include # new import

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('api.urls'))
]
```

Notes:

- path('', include('api.urls')):
  - Any path (hence the blank string)
  - include('api.urls'): Whatever url is sent here... dispatch it and send it over to api.urls

Point the \_\_\_\_ to the View We Created (the 1 endpoint)

- Head to api.urls to

```py

```

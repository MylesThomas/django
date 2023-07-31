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

####

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

```python
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

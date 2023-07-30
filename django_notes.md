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

git config --global user.email "mylescgthomas@gmail.com"
git config --global user.name "mylesthomas"

echo "# django" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/django.git
git push -u origin main
```

- run the shell script:
  - cd django
  - sh setup.sh

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

Goal of this video: Setup the project

- setup project
- understandin how django works
- running on local machine
- server running on local machine

Other videos:

- databases
- templates
- fully functioning websites
- large project
- everything needed to make an actual website

#### Install Django

Install Django with pip:

- pip install django

#### Setup Virtual Environment

Create the virtual environment

- python -m venv
  - python -m venv /path/to/directory

Activate virtual environment

-

Notes: He is working from a virtual environment

- Python's official documentation says: "A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system"

  - when you activate a virtual environment for your project, your project becomes its own self contained application, independent of the system installed Python and its modules
  - Your new virtual environment has its own pip to install libraries, its own libraries folder, where new libraries are added, and its own Python interpreter for the Python version you used to activate the environment.

- The `venv` module supports creating lightweight "virtual environments", each with their own independent set of Python packages installed in their site directories.
  - A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

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

from django.shortcuts import render # was already here
from django.http import HttpResponse # used later in the video

# Create your views here. 
def main(request):
    return HttpResponse("Hello") # this text is what is shown on the webpage when we hit this endpoint 

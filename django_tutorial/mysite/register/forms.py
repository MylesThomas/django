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
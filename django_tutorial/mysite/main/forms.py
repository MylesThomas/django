from django import forms

class CreateNewList(forms.Form): # inherit from Form
    name = forms.CharField(label="Name", max_length=200) # label: what shows up before little box
    check = forms.BooleanField(required=False)
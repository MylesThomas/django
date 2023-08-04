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


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300) 
    complete = models.BooleanField()

    def __str__(self):
        return self.text

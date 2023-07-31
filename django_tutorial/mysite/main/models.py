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
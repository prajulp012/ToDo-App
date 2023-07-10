from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        db_table = 'Todo'
        

class Todoo(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    description = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        db_table = 'Todoo'

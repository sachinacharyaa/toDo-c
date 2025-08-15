from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):  
    title = models.CharField(max_length=100)  
    description = models.TextField(blank=True)  
    status = models.BooleanField(default=False)  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    timestamps = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
      return self.title

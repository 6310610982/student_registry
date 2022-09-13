from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    subjectCode = models.CharField(max_length=5)
    subjectName = models.CharField(max_length=64)
    seat = models.IntegerField(null=True)
    maxSeat = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    state = models.BooleanField(default=None)
    
    
    def __str__(self):
        return f"{self.id}.Code:{self.subjectCode} Name:{self.subjectName} seat:{self.seat}/{self.maxSeat}"
    
        
    
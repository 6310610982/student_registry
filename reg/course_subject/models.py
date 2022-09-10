from django.db import models

# Create your models here.

class Course(models.Model):
    subjectCode = models.CharField(max_length=5)
    subjectName = models.CharField(max_length=64)
    seat = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    state = models.BooleanField(default=None)
    
    
    def __str__(self):
        return f"{self.id}.Code:{self.subjectCode} Subject:{self.subjectName} seat:{self.seat}"
        
    
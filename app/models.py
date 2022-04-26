from django.db import models

# Create your models here. 

from django.urls import reverse

class School(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.id})

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name
        
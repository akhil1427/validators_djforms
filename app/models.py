from django.db import models

# Create your models here.

class school(models.Model):
    Sname=models.CharField(max_length=100)
    Sprinc=models.CharField(max_length=100)
    Sloc=models.CharField(max_length=100)
    Semail=models.EmailField()
    re=models.EmailField()
    def __str__(self):
        return self.Sname

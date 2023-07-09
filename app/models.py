from django.db import models

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    topic = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    
class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    option = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    availability = models.CharField(max_length=255, default=False)
    date = models.DateTimeField(auto_now_add=True)
    
class Ticket(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    ticket = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    comments = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

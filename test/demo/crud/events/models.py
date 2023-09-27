from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=25)
    place = models.CharField(max_length=25)
    city= models.CharField(max_length=25)
    message = models.CharField(max_length=200)
    start_date = models.DateTimeField()


from django.db import models

# Create your models here.
class Item(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    added_by= models.CharField(max_length=50, default=True)
 
    def __str__(self) -> str:
        return self.name
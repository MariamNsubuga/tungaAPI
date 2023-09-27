from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    story = models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
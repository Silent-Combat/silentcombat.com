from django.db import models

class Gallery(models.Model):
    name = models.TextField(max_length=50)
    path = models.TextField()
    
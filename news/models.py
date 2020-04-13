from django.db import models

class Posts(models.Model):
    title = models.TextField()
    date = models.DateField()
    user = models.TextField(default='anonymous')
    post = models.TextField()
from django.db import models

class Servers(models.Model):
    name = models.TextField()
    description = models.TextField()
    address = models.TextField()
    
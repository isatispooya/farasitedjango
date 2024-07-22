from django.db import models

class IntroBanner(models.Model):
    title = models.CharField()
    discription = models.CharField(max_length=100)
    domain = models.CharField(max_length=64, unique=True)
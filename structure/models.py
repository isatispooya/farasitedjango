from django.db import models
from website.models import Domain

class Pop_Up(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/')
    exp_date = models.DateTimeField()
    description = models.CharField(max_length=300)
    Domain =  models.ForeignKey(Domain, on_delete=models.CASCADE)

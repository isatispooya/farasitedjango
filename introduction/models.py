from django.db import models
from website.models import Domain
class IntroBanner(models.Model):
    Title = models.CharField(max_length=500)
    Discription = models.CharField(max_length=500)
    Domain = models.CharField(max_length=64, unique=True)

    def __str__(self) :
        return f'{self.Title}'


class List(models.Model):
    List = models.CharField(max_length=5000)
    

    def __str__(self) :
        return f'{self.List}'
    
class IntroList(models.Model):
    Title = models.CharField(max_length=500)
    List = models.ManyToManyField(List, related_name= 'list_name', blank=True, help_text= 'help', verbose_name = 'introduction of list' )
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.Title}'
    

    
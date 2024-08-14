from django.db import models
from website.models import Domain
from colorfield.fields import ColorField


# super cart
class SuperCart(models.Model):
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Logo = models.ImageField (upload_to='static/images/' , blank=True, null=True)
    Description = models.CharField(max_length=1500)
    Url1 = models.CharField(max_length=500, null=True, blank=True)
    Url2= models.CharField(max_length=500, null=True, blank=True)
    Url3= models.CharField(max_length=500, null=True, blank=True)
    Url4 = models.CharField(max_length=500, null=True, blank=True)
    Url5= models.CharField(max_length=500, null=True, blank=True)
    Url6= models.CharField(max_length=500, null=True, blank=True)
    Url7= models.CharField(max_length=500, null=True, blank=True)
    Url8= models.CharField(max_length=500, null=True, blank=True)
    Url9= models.CharField(max_length=500, null=True, blank=True)
    Url10= models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.Title
    


# roadmap
class Roadmap(models.Model):
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    CartDescription = models.CharField(max_length=1500)
    Sort = models.IntegerField()
    Discription = models.CharField(max_length=1500)
    Color = ColorField (format="hexa" , default='#FFFFFF' , blank=True ,  null= True) 

    def __str__(self):
        return self.Title
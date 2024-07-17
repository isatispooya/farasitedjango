from django.db import models
from website.models import Domain

#sub super product
class SubSuperProduct(models.Model):
    Title = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=1500)
    Url = models.CharField(max_length=500, null=True, blank=True)
    Picture = models.ImageField(upload_to='static/images/',null=True, blank=True)

    def __str__(self):
        return self.Title

# Super Product
class SuperProduct(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.FileField(upload_to='static/images/',null=True, blank=True)
    Description = models.CharField(max_length=1500)
    Domain = models.ForeignKey(Domain, to_field='domain', on_delete=models.CASCADE)
    Super_Product = models.ForeignKey(SubSuperProduct,on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


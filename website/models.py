from django.db import models

# Create your models here.
class Information (models.Model) :
    CreateAt = models.DateTimeField ()
    Logo = models.CharField (max_length=255)
    Logotext = models.CharField (max_length=255)
    Domain = models.CharField (max_length=255)
    Name = models.CharField (max_length=255)
    Telephone = models.CharField (max_length=255)
    Address = models.CharField (max_length=255)
    NationalID = models.CharField (max_length=12)
    AboutUs = models.CharField (max_length=700)
    Theme = models.IntegerField ()
    instagram = models.IntegerField ()
    telegram = models.IntegerField ()
    tweeter = models.IntegerField ()
    Cataloge = models.CharField (max_length=255)
    Description = models.CharField (max_length=500)
    Keywords = models.CharField (max_length=500)
    Admin = models.CharField (max_length=255)
    Date = models.CharField (max_length=255)
    FieldOfActivity = models.CharField (max_length=255)



class ModelBranchesOfCompany (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=255)
    Province = models.CharField (max_length=100)
    City = models.CharField (max_length=100)
    Address = models.CharField (max_length=255)
    Telephone = models.CharField (max_length=20)
    Code = models.CharField (max_length=5)
    Types = models.CharField (max_length=100)
from django.db import models

#Informations
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


# Branchs
class BranchesOfCompany (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=255)
    Province = models.CharField (max_length=100)
    City = models.CharField (max_length=100)
    Address = models.CharField (max_length=255)
    Telephone = models.CharField (max_length=20)
    Code = models.CharField (max_length=5)
    Types = models.CharField (max_length=100)


#BusinessPartners
class BusinessPartners (models.Model) :
    CreateAt = models.DateTimeField()
    Domain =  models.CharField (max_length=255)
    Name =  models.CharField (max_length=255)
    Logo =  models.CharField (max_length=255)
    Link =  models.CharField (max_length=255)



# Contact Us
class ContactUs (models.Model) :
    Name = models.CharField (max_length=255)
    Email = models.CharField (max_length=255)
    Phonenumber = models.CharField (max_length=255)
    # Subject = ListField ()
    Message = models.CharField (max_length=255)
    Domain = models.CharField (max_length=255)
    route = models.CharField (max_length=255)
    CreateAt = models.DateTimeField()



# Email
class Email (models.Model) :
    Domain =  models.CharField (max_length=255)
    CreateAt = models.DateTimeField()
    SenderEmail =  models.CharField (max_length=255)



#Grouping 
class Grouping (models.Model) :
    CreateAt = models.DateTimeField()
    Domain =  models.CharField (max_length=255)
    Title = models.CharField (max_length=255)
    Icone = models.CharField (max_length=255)
    route = models.CharField (max_length=255)
    Url = models.CharField (max_length=255)
    # Status = BooleanField ()


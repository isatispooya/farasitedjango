from django.db import models

#Informations
class Information (models.Model) :
    CreateAt = models.DateTimeField ()
    Logo = models.ImageField (upload_to='static/images/')
    Logotext = models.ImageField (upload_to='static/images/')
    Domain = models.CharField (max_length=255)
    Name = models.CharField (max_length=255)
    Telephone = models.CharField (max_length=255)
    Address = models.CharField (max_length=255)
    NationalID = models.CharField (max_length=12)
    AboutUs = models.CharField (max_length=700)
    Theme = models.IntegerField (blank=True, null=True)
    instagram = models.CharField (max_length=255,blank=True, null=True)
    telegram =models.CharField (max_length=255,blank=True, null=True)
    tweeter = models.CharField (max_length=255,blank=True, null=True)
    Cataloge = models.CharField (max_length=255,blank=True, null=True)
    Description = models.CharField (max_length=500)
    Keywords = models.CharField (max_length=500)
    Admin = models.CharField (max_length=255)
    Date = models.CharField (max_length=255)
    FieldOfActivity = models.CharField (max_length=255)


#Branchs
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



#Contact Us
class ContactUs (models.Model) :
    Name = models.CharField (max_length=255)
    Email = models.CharField (max_length=200)
    Phonenumber = models.CharField (max_length=12)
    Subject = models.CharField (max_length=200)
    Message = models.CharField (max_length=1000)
    Domain = models.CharField (max_length=255)
    route = models.CharField (max_length=255)
    CreateAt = models.DateTimeField()




#Grouping 
class Grouping (models.Model) :
    CreateAt = models.DateTimeField()
    Domain =  models.CharField (max_length=255)
    Title = models.CharField (max_length=255)
    Icone = models.CharField (max_length=255)
    route = models.CharField (max_length=255)
    Url = models.CharField (max_length=255)



#HistoryOfCompanies
class HistoryOfCompanies (models.Model) :
    CreateAt = models.DateTimeField()
    Date = models.CharField (max_length=12)
    Title = models.CharField (max_length=255)
    Paragraph = models.CharField (max_length=700)
    Picture = models.CharField (max_length=255) 
    Video = models.CharField (max_length=255) 
    Domain = models.CharField (max_length=255)
    Icon = models.CharField (max_length=255)


#IntroductionOfCompanies
class IntroductionOfCompanies (models.Model) :
    Logo =models.CharField (max_length=255)
    Name =models.CharField (max_length=255)
    Link =models.CharField (max_length=255)
    Telephone = models.CharField (max_length=12)
    Address = models.CharField (max_length=500)
    ShortAboutUs = models.CharField (max_length=700)
    LongAboutUs = models.CharField (max_length=1500)
    Picture = models.CharField (max_length=255)
    instagram = models.CharField (max_length=255)
    telegram =models.CharField (max_length=255)
    Size = models.IntegerField ()
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=255)




#News
class News (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=255)
    Content = models.CharField (max_length=10000)
    KeyWord = models.CharField (max_length=500)
    Grouping = models.CharField (max_length=255)
    Title = models.CharField (max_length=500)
    TypeOfContent = models.CharField (max_length=255)
    ShortDescription = models.CharField (max_length=700)
    route = models.CharField (max_length=255)
    Picture = models.CharField (max_length=255)



#Products
class Products (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=255)
    Picture =models.CharField (max_length=255)
    Paragraph = models.CharField (max_length=1000)
    Title = models.CharField (max_length=255)
    route = models.CharField (max_length=255)



#Questions
class Questions (models.Model) :
    Question = models.CharField (max_length=500)
    Answer = models.CharField (max_length=1000)
    Domain = models.CharField (max_length=255)
    CreateAt = models.DateTimeField()


#QuickAccess 
class QuickAccess (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=255)
    Url = models.CharField (max_length=255)
    Picture = models.CharField (max_length=255)
    Title = models.CharField (max_length=500)




#RelatedLinks
class RelatedLinks (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=255)
    Link = models.CharField (max_length=255)
    Title = models.CharField (max_length=300)
   

   

#Slider
class Slider (models.Model) :
    Picture = models.CharField (max_length=300)
    Title = models.CharField (max_length=300)
    Alt = models.CharField (max_length=300)
    Domain = models.CharField (max_length=300)
    CreateAt = models.DateTimeField()
    # Status = BooleanField ()


#Statistics
class Statistics (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=300)
    Title = models.CharField (max_length=300)
    Number = models.CharField (max_length=300)
    Icon = models.CharField (max_length=300)
    # Status = BooleanField ()


#TypeOfContent
class TypeOfContent (models.Model) :
    CreateAt = models.DateTimeField()
    Domain = models.CharField (max_length=300)
    Title = models.CharField (max_length=300)
    # Status = BooleanField ()



#Email
class Email (models.Model) :
    Domain =  models.CharField (max_length=255)
    CreateAt = models.DateTimeField()
    SenderEmail =  models.CharField (max_length=255)


#SendEmail
class SendEmail(models.Model):
    Domain = models.CharField (max_length=300)
    CreateAt = models.DateTimeField()
    Recipient = models.CharField (max_length=300)
    Subject = models.CharField (max_length=300)
    Body = models.CharField (max_length=10000)
    SenderEmail = models.CharField (max_length=300)

 
 
#ReceiveEmail
class ReceiveEmail (models.Model) :
    Domain = models.CharField (max_length=255)
    Receiver = models.CharField (max_length=255)
    Sender = models.CharField (max_length=255)
    Body = models.CharField (max_length=10000)
    Subject = models.CharField (max_length=300)
    CreateAt = models.DateTimeField()
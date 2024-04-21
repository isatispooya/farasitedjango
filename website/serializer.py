from rest_framework import serializers
from . import models
from rest_framework import generics


class Information (serializers.ModelSerializer) :
    class Meta:
        model = models.Information
        fields = '__all__' 


class BranchsOfCompany (serializers.ModelSerializer) :
    class Meta:
        model = models.BranchsOfCompany
        fields = '__all__' 

        
class BusinessPartners (serializers.ModelSerializer) :
    class Meta:
        model = models.BusinessPartners
        fields = '__all__' 

class ContactUs (serializers.ModelSerializer) :
    class Meta:
        model = models.ContactUs
        fields = '__all__' 

class Grouping (serializers.ModelSerializer) :
    class Meta:
        model = models.Grouping
        fields = '__all__' 

class HistoryOfCompanies (serializers.ModelSerializer) :
    class Meta:
        model = models.HistoryOfCompanies
        fields = '__all__' 


class ProjectProgress (serializers.ModelSerializer) :
    class Meta:
        model = models.ProjectProgress
        fields = '__all__' 

class IntroductionOfCompanies (serializers.ModelSerializer) :
    class Meta:
        model = models.IntroductionOfCompanies
        fields = '__all__' 

class News (serializers.ModelSerializer) :
    class Meta:
        model = models.News
        fields = '__all__' 

class Products (serializers.ModelSerializer) :
    class Meta:
        model = models.Products
        fields = '__all__' 

class Questions (serializers.ModelSerializer) :
    class Meta:
        model = models.Questions
        fields = '__all__' 

        
class QuickAccess (serializers.ModelSerializer) :
    class Meta:
        model = models.QuickAccess
        fields = '__all__' 

class RelatedLinks (serializers.ModelSerializer) :
    class Meta:
        model = models.RelatedLinks
        fields = '__all__' 



class Subscription (serializers.ModelSerializer) :
    class Meta:
        model = models.Subscription
        fields = '__all__' 



class SubjectSubscription (serializers.ModelSerializer) :
    class Meta:
        model = models.SubjectSubscription
        fields = '__all__' 


class Slider (serializers.ModelSerializer) :
    class Meta:
        model = models.Slider
        fields = '__all__' 


class Statistics (serializers.ModelSerializer) :
    class Meta:
        model = models.Statistics
        fields = '__all__' 


class TypeOfContent (serializers.ModelSerializer) :
    class Meta:
        model = models.TypeOfContent
        fields = '__all__' 



class GalleryVideo (serializers.ModelSerializer) :
    class Meta:
        model = models.GalleryVideo
        fields = '__all__' 



class GalleryPhoto (serializers.ModelSerializer) :
    class Meta:
        model = models.GalleryPhoto
        fields = '__all__' 


class Email (serializers.ModelSerializer) :
    class Meta:
        model = models.Email
        fields = '__all__' 


class SendEmail (serializers.ModelSerializer) :
    class Meta:
        model = models.SendEmail
        fields = '__all__' 


class ReceiveEmail (serializers.ModelSerializer) :
    class Meta:
        model = models.ReceiveEmail
        fields = '__all__' 






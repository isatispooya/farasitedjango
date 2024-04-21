from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializer

# Information 
class InformationViewSet(viewsets.ModelViewSet):
    queryset = models.Information.objects.all()
    serializer_class = serializer.Information
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_object = self.get_queryset().filter(Domain=Domain).last()
        serializer = self.get_serializer(filtered_object)
        return response.Response(serializer.data)

# BranchsOfCompany
class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.BranchsOfCompany.objects.all()
    serializer_class = serializer.BranchsOfCompany
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    
# BusinessPartners
class BusinessPartnersViewSet(viewsets.ModelViewSet):
    queryset = models.BusinessPartners.objects.all()
    serializer_class = serializer.BusinessPartners
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    
# ContactUs
class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializer.ContactUs
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain).last()
        serializer = self.get_serializer(filtered_objects)
        return response.Response(serializer.data)
    
    
# Grouping
class GroupingViewSet(viewsets.ModelViewSet):
    queryset = models.Grouping.objects.all()
    serializer_class = serializer.Grouping
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many=True)
        return response.Response(serializer.data)
    
    
# HistoryOfCompanies
class HistoryOfCompaniesViewSet(viewsets.ModelViewSet):
    queryset = models.HistoryOfCompanies.objects.all()
    serializer_class = serializer.HistoryOfCompanies
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
# ProjectProgress
class ProjectProgressViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectProgress.objects.all()
    serializer_class = serializer.ProjectProgress
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
# IntroductionOfCompanies
class IntroductionOfCompaniesViewSet(viewsets.ModelViewSet):
    queryset = models.IntroductionOfCompanies.objects.all()
    serializer_class = serializer.IntroductionOfCompanies
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
# News
class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializer.News
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
# News With Grouping
class NewsWithGroupingViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializer.News
    def list(self, request):
        Domain = request.query_params.get('Domain')
        grouping = request.query_params.get('grouping')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        if grouping is None:
            raise serializers.ValidationError('Parameter "grouping" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain , Grouping = grouping )
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
# News With Rout
class NewsWithRoutViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializer.News
    def list(self, request):
        Domain = request.query_params.get('Domain')
        route = request.query_params.get('route')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        if route is None:
            raise serializers.ValidationError('Parameter "route" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain , route = route).last()
        serializer = self.get_serializer(filtered_objects)
        return response.Response(serializer.data)
    



# Products
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializer.Products
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    



# SoloProducts
class SoloProductsViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializer.Products
    def list(self, request):
        Domain = request.query_params.get('Domain')
        route = request.query_params.get('route')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        if route is None:
            raise serializers.ValidationError('Parameter "route" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain , route=route ).last()
        serializer = self.get_serializer(filtered_objects)
        return response.Response(serializer.data)
    


    
# Questions
class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    serializer_class = serializer.Questions
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
# QuickAccess
class QuickAccessViewSet(viewsets.ModelViewSet):
    queryset = models.QuickAccess.objects.all()
    serializer_class = serializer.QuickAccess
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
# RelatedLinks
class RelatedLinksViewSet(viewsets.ModelViewSet):
    queryset = models.RelatedLinks.objects.all()
    serializer_class = serializer.RelatedLinks
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    

    
    
    
# SubjectSubscription
class SubjectSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = models.SubjectSubscription.objects.all()
    serializer_class = serializer.SubjectSubscription
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    

    
# Subscription
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = models.Subscription.objects.all()
    serializer_class = serializer.Subscription
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
# Slider
class SliderViewSet(viewsets.ModelViewSet):
    queryset = models.Slider.objects.all()
    serializer_class = serializer.Slider
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
# Statistics
class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = models.Statistics.objects.all()
    serializer_class = serializer.Statistics
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
# TypeOfContent
class TypeOfContentViewSet(viewsets.ModelViewSet):
    queryset = models.TypeOfContent.objects.all()
    serializer_class = serializer.TypeOfContent
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
    
    
    
    
# GalleryPhoto
class GalleryPhotoViewSet(viewsets.ModelViewSet):
    queryset = models.GalleryPhoto.objects.all()
    serializer_class = serializer.GalleryPhoto
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
    
    
    
    
# GalleryVideo
class GalleryVideoViewSet(viewsets.ModelViewSet):
    queryset = models.GalleryVideo.objects.all()
    serializer_class = serializer.GalleryVideo
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    
    
    
    
    
# Email
class EmailViewSet(viewsets.ModelViewSet):
    queryset = models.Email.objects.all()
    serializer_class = serializer.Email
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects)
        return response.Response(serializer.data)
    
    
    
    
    
# SendEmail
class SendEmailViewSet(viewsets.ModelViewSet):
    queryset = models.SendEmail.objects.all()
    serializer_class = serializer.SendEmail
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects)
        return response.Response(serializer.data)
    
    
    
    
    
# ReceiveEmail
class ReceiveEmailViewSet(viewsets.ModelViewSet):
    queryset = models.ReceiveEmail.objects.all()
    serializer_class = serializer.ReceiveEmail
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializer
import datetime
import pandas as pd
from random import sample , randint

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

# Branchs Of Company
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
    
# Business Partners
class BusinessPartnersViewSet(viewsets.ModelViewSet):
    queryset = models.BusinessPartners.objects.all()
    serializer_class = serializer.BusinessPartners
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
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
        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
        serializer = self.get_serializer(filtered_objects , many=True)
        return response.Response(serializer.data)
    
    
# History Of Companies
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
    
  
    
# Project Progress
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
    
    
# Introduction Of Companies
class IntroductionOfCompaniesViewSet(viewsets.ModelViewSet):
    queryset = models.IntroductionOfCompanies.objects.all()
    serializer_class = serializer.IntroductionOfCompanies
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        df = pd.DataFrame(serializer.data)
        if len(df)==0:
            return response.Response([])

        df = df.sample(frac=1).reset_index(drop=True)
        df = df[df.index<=20]
        df['Size']= [randint(1,3) for x in df.index]
        while df['Size'].sum () != 24 :
            inx = randint(0,df.index.max()*1)
            sumsize = df['Size'].sum ()
            Size = df['Size'][inx]
            Increase = sumsize < 24 
            Decrease = sumsize > 24
            if Increase and  Size < 3 :
                df['Size'][inx] = Size+1
            elif Decrease and Size > 1 :
                df['Size'][inx] = Size-1
        df = df.to_dict('records')
        return response.Response(df)
    
    
# News
class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializer.News
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain , show = True)
        serializer = self.get_serializer(filtered_objects , many = True)


        return response.Response(serializer.data)
    

# Content Tabs
class ContentTabsViewSet(viewsets.ModelViewSet):
    queryset = models.ContentTabs.objects.all()
    serializer_class = serializer.ContentTabs
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializerz = self.get_serializer(filtered_objects , many = True)

        tabs = pd.DataFrame(serializerz.data)
        tabs['children'] = [[] for x in tabs.index]

        for i in tabs.index:
            id = tabs['id'][i]
            Qa_modal = models.QaOfContentTabs.objects.filter(ContentTabs=id)
            Qa_serializ = serializer.QaOfContentTabs(Qa_modal,many = True).data
            Qa_df = pd.DataFrame(Qa_serializ)[['TitleTab','Question','Answer','Image','Link']]
            Qa_dic = Qa_df.to_dict('records')
            tabs['children'][i] = Qa_dic
        tabs = tabs.to_dict('records')
        return response.Response(tabs)


# Comparison
class ContentComparisonViewSet(viewsets.ModelViewSet):
    queryset = models.ContentComparison.objects.all()
    serializer_class = serializer.ContentComparison
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializerz = self.get_serializer(filtered_objects , many = True)
        tabs = pd.DataFrame(serializerz.data)
        tabs['children'] = [[] for x in tabs.index]
        for i in tabs.index:
            id = tabs['id'][i]
            Qa_modal = models.ContentComparisonBtn.objects.filter(ContentTabs=id)
            Qa_serializ = serializer.ContentComparisonBtn(Qa_modal,many = True).data
            Qa_df = pd.DataFrame(Qa_serializ)[['Title','Description','Image']]
            Qa_dic = Qa_df.to_dict('records')
            tabs['children'][i] = Qa_dic
        tabs = tabs.to_dict('records')
        return response.Response(tabs)


# Content List
class ContentListViewSet(viewsets.ModelViewSet):
    queryset = models.ContentList.objects.all()
    serializer_class = serializer.ContentList
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializerz = self.get_serializer(filtered_objects , many = True)
        tabs = pd.DataFrame(serializerz.data)
        tabs['children'] = [[] for x in tabs.index]
        for i in tabs.index:
            id = tabs['id'][i]
            Qa_modal = models.ContentListChild.objects.filter(ContentTabs=id)
            Qa_serializ = serializer.ContentListChild(Qa_modal,many = True).data
            Qa_df = pd.DataFrame(Qa_serializ)[['Title','Description','Icon']]
            Qa_dic = Qa_df.to_dict('records')
            tabs['children'][i] = Qa_dic
        tabs = tabs.to_dict('records')
        return response.Response(tabs)


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
    

# Solo Products
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
    
   
# Quick Access
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
    
       
# Related Links
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
    
   
# Subject Subscription
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

    def create(self, request, *args, **kwargs):
        Domain = request.data.get('Domain')
        Telephone = request.data.get('Telephone')
        Subject = request.data.get('Subject')
        CreateAt = datetime.datetime.now()
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        subscription = models.Subscription(Domain=Domain, Telephone=Telephone, Subject=Subject, CreateAt=CreateAt)
        subscription.save()

        return response.Response({"success": True})

    
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
    
    
# Type Of Content
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
    
   
# Gallery Photo
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

    
# Gallery Video
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
    
   
# Chart
class ChartViewSet(viewsets.ModelViewSet):
    queryset = models.positionofmanagers.objects.all()
    serializer_class = serializer.positionofmanagers
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializerz = self.get_serializer(filtered_objects , many = True)
        
        filtered_objects_ManagersPeople = models.ManagersPeople.objects.all()
        serializer_ManagersPeople = serializer.ManagersPeople(filtered_objects_ManagersPeople, many=True)

        df = pd.DataFrame(serializerz.data)
        df = df.sort_values(by='Level')
        df['Senior'] = df['Senior'].fillna('NoSenior')
        df_root = df[df['Senior']=='NoSenior']
        dff = pd.DataFrame(serializer_ManagersPeople.data)


        result = []

        for i in df_root.index:
            pos = df['id'][i]
            posName = df[df['id']==pos].to_dict('records')[0]['Title']
            personal = dff[dff['Position'] == pos].to_dict('records')
            poss_child = list(set(df[df['Senior']== posName]['id']))
            child = []
            for j in poss_child:

                print(j)
                print(dff)
                personal_child = dff[dff['Position'] == j].to_dict('records')
                child_dic = {'pos':j, 'personal':personal_child}
                child.append(child_dic)

            dic = {'pos':pos, 'personal':personal, 'children':child}
            result.append(dic)

        return response.Response(result) 
    

# Menu
class MenuViewSet(viewsets.ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializer.Menu
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many=True)
        df = pd.DataFrame(serializer.data)
        df = df.sort_values(by="Sort",ascending=False)

        result = []
        for i in list ( set (df['MegaMenu'])) :
            SubMenu = df[df['MegaMenu']== i ]
            MegaSort = SubMenu['Sort'].mean()
            SubMenu = SubMenu.to_dict ("records")

            result.append ({'MegaMenu':i,'MegaSort' : MegaSort ,'SubMenu':SubMenu})
        
        result = pd.DataFrame(result).sort_values('MegaSort',ascending=False)
        result = result.to_dict('records')



        return response.Response(result)
    
       
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
       
    
# Send Email
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
    
 
# Receive Email
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
    


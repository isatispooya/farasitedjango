from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('information', views.InformationViewSet)
router.register('branch', views.BranchViewSet)
router.register('businessPartners', views.BusinessPartnersViewSet)
router.register('contactus', views.ContactUsViewSet)
router.register('grouping', views.GroupingViewSet)
router.register('historyofcompanies', views.HistoryOfCompaniesViewSet)
router.register('introductionofcompanies', views.IntroductionOfCompaniesViewSet)
router.register('news', views.NewsViewSet)
router.register('products', views.ProductsViewSet)
router.register('soloProducts', views.SoloProductsViewSet)
router.register('questions', views.QuestionsViewSet)
router.register('quickaccess', views.QuickAccessViewSet)
router.register('relatedlinks', views.RelatedLinksViewSet)
router.register('slider', views.SliderViewSet)
router.register('statistics', views.StatisticsViewSet)
router.register('galleryphoto', views.GalleryPhotoViewSet)
router.register('galleryvideo', views.GalleryVideoViewSet)
router.register('typeofcontent', views.TypeOfContentViewSet)
router.register('email', views.EmailViewSet)
router.register('sendemail', views.SendEmailViewSet)
router.register('receiveemail', views.ReceiveEmailViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

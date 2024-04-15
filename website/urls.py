from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(viewset=views.InformationViewSet, prefix='information', basename='information')
router.register(viewset=views.BranchViewSet ,prefix='branch',basename='branch')
router.register(viewset=views.BusinessPartnersViewSet ,prefix='businessPartners',basename='businessPartners')
router.register(viewset=views.ContactUsViewSet ,prefix='contactus',basename='contactus')
router.register(viewset=views.GroupingViewSet ,prefix='grouping',basename='grouping')
router.register(viewset=views.HistoryOfCompaniesViewSet ,prefix='historyofcompanies',basename='historyofcompanies')
router.register(viewset=views.IntroductionOfCompaniesViewSet ,prefix='introductionofcompanies',basename='introductionofcompanies')
router.register(viewset=views.NewsViewSet ,prefix='news',basename='news')
router.register(viewset=views.ProductsViewSet, prefix='products',basename='products')
router.register(viewset=views.SoloProductsViewSet, prefix='soloproducts', basename='solo_products')
router.register(viewset=views.QuestionsViewSet ,prefix='questions', basename='questions')
router.register(viewset=views.QuickAccessViewSet ,prefix='quickaccess',basename='quickaccess')
router.register(viewset=views.RelatedLinksViewSet ,prefix='relatedlinks',basename='relatedlinks')
router.register(viewset=views.SliderViewSet ,prefix='slider',basename='slider')
router.register(viewset=views.StatisticsViewSet ,prefix='statistics',basename='statistics')
router.register(viewset=views.GalleryPhotoViewSet ,prefix='galleryphoto',basename='galleryphoto')
router.register(viewset=views.GalleryVideoViewSet ,prefix='galleryvideo',basename='galleryvideo')
router.register(viewset=views.TypeOfContentViewSet ,prefix='typeofcontent',basename='typeofcontent')
router.register(viewset=views.EmailViewSet ,prefix='email',basename='email')
router.register(viewset=views.SendEmailViewSet ,prefix='sendemail',basename='sendemail')
router.register(viewset=views.ReceiveEmailViewSet ,prefix='receiveemail',basename='receiveemail')
router.register(viewset=views.NewsWithRoutViewSet ,prefix='newswithroute',basename='newswithroute')
router.register(viewset=views.NewsWithGroupingViewSet ,prefix='newswithgrouping',basename='newswithgrouping')


urlpatterns = [
    path('', include(router.urls)),
]

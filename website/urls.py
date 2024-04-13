from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('information', views.InformationViewSet)
router.register('branche', views.BrancheViewSet)
router.register('BusinessPartners', views.BusinessPartnersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

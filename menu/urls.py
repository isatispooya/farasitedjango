from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(viewset=views.SuperMenuViewSet ,prefix='SuperMenus',basename='SuperMenus')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'superproduct', views.SuperProductViewSet, basename='superproduct')

urlpatterns = [
    path('', include(router.urls)),
]

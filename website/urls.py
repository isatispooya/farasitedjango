from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('information', views.information)
router.register('branche', views.branche)

urlpatterns = [
    path('', include(router.urls)),
]

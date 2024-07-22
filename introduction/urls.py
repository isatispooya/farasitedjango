from django.urls import path, include
from . import views
from website.urls import router



router.register(viewset=views.IntrocardViewSet ,prefix='introcard',basename='introcard')

urlpatterns = [
    path('', include(router.urls)),
]

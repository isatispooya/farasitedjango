from django.urls import path, include
from . import views
from website.urls import router





router.register(viewset=views.Pop_UpViewset, prefix='Pop_Up', basename='Pop_Up')


urlpatterns = [
    path('', include(router.urls)),

]
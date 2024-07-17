from django.urls import path, include
from . import views
from website.urls import routers


router = routers.DefaultRouter()

router.register(viewset=views.SuperProductViewset ,prefix='superproduct',basename='superproduct')


urlpatterns = [
    path('', include(router.urls)),

]

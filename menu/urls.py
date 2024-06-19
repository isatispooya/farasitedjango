from django.urls import path, include
from . import views
from website.urls import router



router.register(viewset=views.SuperMenuViewSet ,prefix='supermenus',basename='supermenus')

urlpatterns = [
    path('', include(router.urls)),
]

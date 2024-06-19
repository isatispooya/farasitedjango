from rest_framework import viewsets
from .models import SubSuperMenu, SuperMenu
from .serializers import  SubSuperMenuSerializer, SuperMenuSerializer


class SubSuperMenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubSuperMenu.objects.all()
    serializer_class = SubSuperMenuSerializer

class SuperMenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SuperMenu.objects.all()
    serializer_class = SuperMenuSerializer

from rest_framework import viewsets
from .models import  SuperMenu
from .serializers import SuperMenuSerializer
from rest_framework import serializers


class SuperMenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SuperMenu.objects.all()
    serializer_class = SuperMenuSerializer
    
    def get_queryset(self):
        domain = self.request.query_params.get('domain')
        if not domain:
            raise serializers.ValidationError({'domain': 'این پارامتر الزامی است.'})
        return super().get_queryset().filter(domain=domain).order_by('sort')
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


from rest_framework import viewsets
from .models import SubSuperMenu, SuperMenu
from .serializers import  SubSuperMenuSerializer, SuperMenuSerializer
from rest_framework import serializers
from rest_framework import response


class SubSuperMenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubSuperMenu.objects.all()
    serializer_class = SubSuperMenuSerializer

class SuperMenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SuperMenu.objects.all()
    serializer_class = SuperMenuSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    
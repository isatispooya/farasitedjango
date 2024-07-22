from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializers


class IntrocardViewSet(viewsets.ModelViewSet):
    queryset = models.Introcard.objects.all()
    serializer_class = serializers.Introcard
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects)
        return response.Response(serializer.data)
    
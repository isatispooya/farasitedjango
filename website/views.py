from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from . import models
from . import serializer

# Create your views here.
class SetUpInformation(viewsets.ModelViewSet):
    queryset = models.Information.objects.all()
    serializer_class = serializer.Information
    def get(self, request):
        domin = request.query_params.get('Domin')
        if domin is None:
            raise serializers.ValidationError('Parameter "domin" is required.')

        return models.objects.filter(Domin=domin).last()


from django.shortcuts import render
from . import serializer
from rest_framework import viewsets
from . import models
from rest_framework import serializers
from rest_framework import response


class SuperProductViewset(viewsets.ModelViewSet):
    queryset = models.SuperProduct.objects.all() 
    serializer_class = serializer.SuperProduct
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects , many = True)
        return response.Response(serializer.data)
    

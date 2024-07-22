from django.shortcuts import render
from rest_framework import viewsets
from .models import IntroBanner,IntroList,List
from .serializers import  IntroBannerSerializer, IntroListSerializer, ListSerializer
from rest_framework import serializers
from rest_framework import response

class IntroBannerViewset(viewsets.ModelViewSet):
    queryset = IntroBanner.objects.all()
    serializer_class = IntroBannerSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    

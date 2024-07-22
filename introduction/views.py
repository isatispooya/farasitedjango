from django.shortcuts import render
from rest_framework import viewsets
from .models import IntroBanner,IntroList, Introcard
from .serializers import  IntroBannerSerializer,IntrocardSerializer,IntroListSerializer
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
    


class IntrocardViewSet(viewsets.ModelViewSet):
    queryset = Introcard.objects.all()
    serializer_class = IntrocardSerializer
    serializer_class = IntrocardSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects)
        return response.Response(serializer.data)

class IntroListViewset(viewsets.ModelViewSet):
    queryset = IntroList.objects.all()
    serializer_class = IntroListSerializer
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        print(Domain)

        filtered_objects = self.get_queryset().filter(Domain__domain=Domain)
        print(filtered_objects)
        
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    


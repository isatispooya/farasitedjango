from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializer

# Create your views here.
class information(viewsets.ModelViewSet):
    queryset = models.Information.objects.all()
    serializer_class = serializer.Information
    def get(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        print('ssss',Domain)
        filtered_object = self.get_queryset().filter(Domain=Domain).last()
        # سریال کردن شیء فیلتر شده
        serializer = self.get_serializer(filtered_object)
        return response.Response(serializer.data)


class branche(viewsets.ModelViewSet):
    queryset = models.BranchesOfCompany.objects.all()
    serializer_class = serializer.BranchesOfCompany
    def get(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')

        return models.objects.filter(Domin=Domain).last()

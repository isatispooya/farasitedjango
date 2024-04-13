from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializer


class InformationViewSet(viewsets.ModelViewSet):
    queryset = models.Information.objects.all()
    serializer_class = serializer.Information
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_object = self.get_queryset().filter(Domain=Domain).last()
        serializer = self.get_serializer(filtered_object)
        return response.Response(serializer.data)


class BrancheViewSet(viewsets.ModelViewSet):
    queryset = models.BranchesOfCompany.objects.all()
    serializer_class = serializer.BranchesOfCompany
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
    

class BusinessPartnersViewSet(viewsets.ModelViewSet):
    queryset = models.BusinessPartners.objects.all()
    serializer_class = serializer.BusinessPartners
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_objects = self.get_queryset().filter(Domain=Domain)
        serializer = self.get_serializer(filtered_objects, many=True)
        return response.Response(serializer.data)
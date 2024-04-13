from rest_framework import serializers
from . import models
from rest_framework import generics


class Information (serializers.ModelSerializer) :
    class Meta:
        model = models.Information
        fields = '__all__' 


class BranchesOfCompany (serializers.ModelSerializer) :
    class Meta:
        model = models.BranchesOfCompany
        fields = '__all__' 
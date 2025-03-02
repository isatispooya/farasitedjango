from rest_framework import serializers
from . import models


class SuperCart (serializers.ModelSerializer) :
    class Meta:
        model = models.SuperCart
        fields = '__all__' 

class Roadmap (serializers.ModelSerializer) :
    class Meta:
        model = models.Roadmap
        fields = '__all__' 

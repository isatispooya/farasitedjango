from rest_framework import serializers
from . import models

class SubSuperProduct(serializers.ModelSerializer):
    class Meta:
        model = models.SubSuperProduct
        fields = '__all__' 


class SuperProduct(serializers.ModelSerializer):
    # sub = SubSuperProduct(many = True)
    class Meta:
        model = models.SuperProduct
        fields = '__all__' 
  



from rest_framework import serializers
from .models import IntroBanner, IntroList, List

class IntroBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroBanner
        fields = '__all__'

class IntroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroList
        fields = '__all__'        

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'              
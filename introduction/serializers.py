from rest_framework import serializers
from .models import IntroBanner, IntroList, List , Card , Introcard

class IntroBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroBanner
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'   
        
                   
class IntroListSerializer(serializers.ModelSerializer):
    list = ListSerializer(many = True)
    class Meta:
        model = IntroList
        fields = '__all__'        



class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'              


class IntrocardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introcard
        fields = '__all__'              
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




class IntrocardSerializer(serializers.ModelSerializer):
    Card = serializers.SerializerMethodField()

    class Meta:
        model = Introcard
        fields = ['id', 'Title', 'Domain', 'Card']
    def get_Card(self, obj):
        return [card.Card for card in obj.Card.all()]
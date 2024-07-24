from rest_framework import serializers
from .models import Content, Introduction, Card, Sections


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = ['Title', 'Description']



class ContentSerializer(serializers.ModelSerializer):
    Introduction = IntroductionSerializer (many = True)
    class Meta:
        model = Content
        fields = ['Name', 'Introduction']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['Title', 'Description']

class SectionsSerializer(serializers.ModelSerializer):
    Card = CardSerializer(many = True)
    Content = ContentSerializer(many = True)
    class Meta:
        model = Sections
        fields = ['Title', 'Content', 'Card', 'Domain']
        
from rest_framework import serializers
from .models import Content, Introduction, Card, Sections


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['Name', 'Introduction']


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = ['Title', 'Description']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['Title', 'Description']


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['Title', 'Content', 'Card', 'Domain']
        
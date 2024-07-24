from rest_framework import serializers
from .models import Content, Introduction


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['Name', 'Introduction']


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = ['Title', 'Description']

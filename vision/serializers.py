from rest_framework import serializers
from .models import ContentDrop , TabVision

class ContentDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDrop
        fields = ['Title' , 'Summer']


class TabvisionSerializer(serializers.ModelSerializer):
    Contentdrop = ContentDropSerializer(many = True)
    class Meta:
        model = TabVision
        fields = ['Title' , 'Summer' , 'Contentdrop' , 'Domain']
from rest_framework import serializers
from .models import ContentDrop

class ContentDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentDrop
        fields = '__all__'


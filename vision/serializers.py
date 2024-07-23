from rest_framework import serializers
from .models import ContextDrop

class ContextDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextDrop
        fields = '__all__'
        
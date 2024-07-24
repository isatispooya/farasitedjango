from rest_framework import serializers
from .models import List, Card, Number, Brief


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['Title', 'Description']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['Title', 'Description']

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['Title', 'Number', 'Little']

class BriefSerializer(serializers.ModelSerializer):
    List = ListSerializer(many = True)
    Card = CardSerializer(many = True)
    Number = NumberSerializer(many = True)

    class Meta:
        model = Brief
        fields = ['Title','Description', 'Question','Domain', 'List', 'Card', 'Number']



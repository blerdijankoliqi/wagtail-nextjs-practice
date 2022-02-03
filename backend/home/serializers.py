from dataclasses import fields
from rest_framework import serializers
from .models import HomePage

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


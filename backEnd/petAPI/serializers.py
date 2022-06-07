from dataclasses import fields
from rest_framework import serializers
from petAPI.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'created', 'name', 'age', 'availability', 'photoUrl', ]

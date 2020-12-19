from django.db.models import fields
from rest_framework import serializers
from . import models
class PersoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persone
        fields = ['pk', 'name']
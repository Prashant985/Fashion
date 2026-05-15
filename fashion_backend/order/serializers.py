from rest_framework import serializers
from . import models

class OrderSerializer(serializers.Serializer):
    class Meta:
        model = models.Order
        fields = '__all__'
        
from rest_framework import serializers
from . import models
from core.serializers import ProductSerializer

class CartSerializer(serializers.Serializer):
    product = ProductSerializer(read_only = True)
    exclude = ['userId', 'created_at', 'updated_at']
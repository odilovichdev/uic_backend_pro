from rest_framework import serializers

from apps.order.models import Product

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "name", "price", "is_active", "image")
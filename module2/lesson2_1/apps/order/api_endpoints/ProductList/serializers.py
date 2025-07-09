from rest_framework import serializers

from apps.order.models import Product, OrderItem, OrderItemConfig


class ProductOrderItemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemConfig
        fields = ("key", "value")


class ProductOrderItemSerializer(serializers.ModelSerializer):
    configurations = ProductOrderItemConfigSerializer(many=True, read_only=True)
 
    class Meta:
        model = OrderItem
        fields = ("id", "quantity", "configurations")


class ProductListSerializer(serializers.ModelSerializer):
    order_items = ProductOrderItemSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "price", "is_active", "image", "order_items")
from rest_framework import serializers

from apps.order.models import Product, OrderItem, OrderItemConfig


class ProductOrderItemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemConfig
        fields = ("id", "key", "value")


class ProductOrderItemSerializer(serializers.ModelSerializer):
    configurations = ProductOrderItemConfigSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ("order", "quantity", "configurations")


class ProductListSerializer(serializers.ModelSerializer):
    order_lists = ProductOrderItemSerializer(source='order_items', many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "price", "is_active", "image", "order_lists")
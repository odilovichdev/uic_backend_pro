from rest_framework import serializers

from apps.order.models import OrderItem, Order, Product


class OrderItemCreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "name", "user", "created_at")


class OrderItemCreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "is_active", "image")


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "order",
            "quantity"
        )
    

    def to_internal_value(self, data):
        print(data, "Called to_internal_value")
        result = super().to_internal_value(data)
        print(result, "Called to_internal_value to super")
        return result
    

    def to_representation(self, instance):
        print(instance, "Called to_reprizantion")
        result = super().to_representation(instance) 
        result['order'] = OrderItemCreateOrderSerializer(instance.order).data
        result['product'] = OrderItemCreateProductSerializer(instance.product).data
        print(result, "Called to_reprizantion to super")
        return result
    

    def validate(self, attrs):
        print(attrs, "Called validated")
        return attrs
    
    def validate_quantity(self, value):
        print(value, "Called validated field")
        return value
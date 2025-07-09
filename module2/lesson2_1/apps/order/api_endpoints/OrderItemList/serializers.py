from rest_framework import serializers

from apps.order.models import OrderItem, Order, Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("name", "user")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "price")


class OrderItemListSerializers(serializers.ModelSerializer):
    product_data = ProductSerializer(read_only=True, source="product")
    order_data = OrderSerializer(read_only=True, source="order")
    # order = serializers.SerializerMethodField(method_name='get_order')
    # product = serializers.SerializerMethodField(method_name="get_product")

    class Meta:
        model = OrderItem
        fields = ("id", "product", "product_data", "order", "order_data", "quantity")
        extra_kwargs = {
            "order": {"write_only": True},
            "product": {"write_only": True}
        }

    # def get_order(self, obj):
    #     return OrderSerializer(obj.order).data if obj.order else None
    #
    # def get_product(self, obj):
    #     return ProductSerializer(obj.product).data if obj.product else None







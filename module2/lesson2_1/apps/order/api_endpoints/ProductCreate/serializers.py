from rest_framework import serializers

from apps.order.models import Product


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "is_active", "image")

    def validate(self, attrs):

        if attrs.get("price") < 0:
            raise serializers.ValidationError({"price": "Price 0 dan kichik bo'lishi mumkin emas."})

        if attrs.get("name") and len(attrs.get('name')) < 3:
            raise serializers.ValidationError({"name":"Product name uzunligi 3 ta harfdan kichik bo'lishi mumkin emas."})

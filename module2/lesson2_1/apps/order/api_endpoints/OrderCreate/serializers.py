from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.order.models import Order


class OrderCreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")


class OrderCreateSerializer(serializers.ModelSerializer):
    user = OrderCreateUserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "name", "user", "created_at")

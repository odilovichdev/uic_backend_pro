from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.order.models import Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")


class OrderListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "name", "user", "created_at")

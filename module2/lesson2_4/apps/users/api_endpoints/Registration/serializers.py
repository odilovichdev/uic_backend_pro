from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)

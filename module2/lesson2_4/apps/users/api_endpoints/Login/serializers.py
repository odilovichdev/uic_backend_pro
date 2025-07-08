from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    session = serializers.CharField()
    code = serializers.CharField()

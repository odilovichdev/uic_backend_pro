from django.core.cache import cache
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError

from apps.users.utils import generate_cache_key
from apps.users.api_endpoints.Login.serializers import LoginSerializer


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get("phone_number")
        session = serializer.validated_data.get("session")
        code = serializer.validated_data.get("code")

        cache_key = generate_cache_key(phone_number, session)

        if cache.get(cache_key) != code:
            raise ValidationError("Invalid session or code")

        user, _ = get_user_model().objects.get_or_create(phone_number=phone_number)
        cache.delete(cache_key)

        return Response(user.token)


__all__ = [
    "LoginAPIView",
]

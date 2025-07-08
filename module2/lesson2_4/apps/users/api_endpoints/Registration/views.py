from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import ValidationError

from apps.users.api_endpoints.Registration.serializers import RegisterSerializer
from apps.users.tasks import send_single_sms_task
from apps.users.utils import generate_cache_key, generate_session, generate_code, send_single_sms


class RegisterSentSmsAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        phone_number = serializer.validated_data.get("phone_number", None)

        cache_key = generate_cache_key(phone_number)

        # if cache.keys(f'{cache_key}*'):
        #     raise ValidationError("Already sent sms")

        session = generate_session(session_length=16)
        code = generate_code()

        cache_key = generate_cache_key(phone_number, session)
        cache.set(cache_key, code, timeout=60)

        send_single_sms_task.delay(phone_number, code)

        return Response({"phone_number": phone_number, "session": session})


__all__ = [
    "RegisterSentSmsAPIView",
]

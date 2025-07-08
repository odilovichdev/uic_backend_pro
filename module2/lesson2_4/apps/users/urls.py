from django.urls import path

from apps.users.api_endpoints import (
    RegisterSentSmsAPIView, LoginAPIView
)

app_name = 'users'

urlpatterns = [
    path("register", RegisterSentSmsAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
]

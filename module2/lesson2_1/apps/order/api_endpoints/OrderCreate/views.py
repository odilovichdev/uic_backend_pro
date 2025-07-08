from rest_framework.generics import CreateAPIView

from apps.order.api_endpoints.OrderCreate.serializers import OrderCreateSerializer
from apps.order.models import Order


class OrderCreateAPIView(CreateAPIView):
    queryset = Order
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = [
    "OrderCreateAPIView"
]

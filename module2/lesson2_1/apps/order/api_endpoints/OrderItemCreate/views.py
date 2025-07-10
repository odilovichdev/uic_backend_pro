from rest_framework.generics import CreateAPIView

from apps.order.models import OrderItem
from apps.order.api_endpoints.OrderItemCreate.serializers import OrderItemCreateSerializer


class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateSerializer



__all__ = [
    "OrderItemCreateAPIView"
]


    
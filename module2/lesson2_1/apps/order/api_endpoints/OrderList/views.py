from rest_framework.generics import ListAPIView

from apps.order.api_endpoints.OrderList.serializers import OrderListSerializer
from apps.order.models import Order


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


__all__ = [
    "OrderListAPIView"
]

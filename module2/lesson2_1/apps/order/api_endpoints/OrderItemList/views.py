from rest_framework.generics import ListAPIView, ListCreateAPIView

from apps.order.models import OrderItem
from apps.order.api_endpoints.OrderItemList.serializers import OrderItemListSerializers


class OrderItemListAPIView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializers


__all__ = [
    "OrderItemListAPIView",
]

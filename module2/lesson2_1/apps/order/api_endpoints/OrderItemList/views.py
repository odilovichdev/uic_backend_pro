from rest_framework.generics import ListAPIView, ListCreateAPIView

from apps.order.models import OrderItem
from apps.order.api_endpoints.OrderItemList.serializers import OrderItemListSerializers


class OrderItemListAPIView(ListCreateAPIView):
    queryset = OrderItem.objects.select_related("product", "order").only("id", "quantity", "product__name", "product__price", "order__name", "order__user")
    serializer_class = OrderItemListSerializers


__all__ = [
    "OrderItemListAPIView",
]

from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from apps.order.models import Product, OrderItem, OrderItemConfig
from apps.order.api_endpoints.ProductList.serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.prefetch_related(
        Prefetch(
            "order_items",
            queryset=OrderItem.objects.prefetch_related(Prefetch("configurations", queryset=OrderItemConfig.objects.only('key', "value", "order_item"))).only("id", "quantity", "product")
        ), 
        # Prefetch(
        #     "order_items__configurations",
        #     queryset=OrderItemConfig.objects.only("key", "value", "order_item")
        # )
        )
    serializer_class = ProductListSerializer


__all__ = [
    "ProductListAPIView"
]
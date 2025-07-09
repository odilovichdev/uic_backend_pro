from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from apps.order.models import Product
from apps.order.api_endpoints.ProductList.serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.prefetch_related("order_items", "order_items__configurations")
    serializer_class = ProductListSerializer


__all__ = [
    "ProductListAPIView"
]
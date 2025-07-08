from rest_framework.generics import ListAPIView

from apps.order.models import Product
from apps.order.api_endpoints.ProductList.serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


__all__ = [
    "ProductListAPIView"
]
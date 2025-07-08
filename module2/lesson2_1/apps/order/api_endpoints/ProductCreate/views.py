from rest_framework.generics import CreateAPIView

from apps.order.api_endpoints.ProductCreate.serializers import ProductCreateSerializer
from apps.order.models import Product


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


__all__ = [
    "ProductCreateAPIView"
]

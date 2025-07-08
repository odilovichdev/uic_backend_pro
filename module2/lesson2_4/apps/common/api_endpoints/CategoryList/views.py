from rest_framework.generics import ListAPIView

from apps.common.api_endpoints.CategoryList.serializers import CategoryListSerializer
from apps.common.models import Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


__all__ = [
    "CategoryListAPIView",
]

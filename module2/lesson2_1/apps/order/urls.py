from django.urls import path

from apps.order.api_endpoints import (
    ProductListAPIView,
    OrderItemListAPIView,
    ProductCreateAPIView,
    OrderListAPIView,
    OrderCreateAPIView,
)

app_name = "order"

urlpatterns = [
    path("product-list", ProductListAPIView.as_view(), name="product-list"),
    path("order-item-list", OrderItemListAPIView.as_view(), name="order-item-list"),
    path("product-create", ProductCreateAPIView.as_view(), name="product-create"),
    path("order-list", OrderListAPIView.as_view(), name="order-list"),
    path("order-create", OrderCreateAPIView.as_view(), name="order-create"),
]

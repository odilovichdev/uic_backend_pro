from django.contrib import admin

from .models import Product, Order, OrderItem, OrderItemConfig


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItemConfig)
class OrderItemConfigAdmin(admin.ModelAdmin):
    pass

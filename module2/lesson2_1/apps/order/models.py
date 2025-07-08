from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    is_active = models.BooleanField(_("is Active"), default=False)
    image = models.ImageField(_("Image"), null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
                             related_name="orders")
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)


    def __str__(self):
        return f"{self.name}"


class OrderItem(models.Model):
    order = models.ForeignKey("order.Order", on_delete=models.CASCADE, 
                            related_name="order_items")
    product = models.ForeignKey("order.Product", on_delete=models.CASCADE,
                            related_name="order_items")
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), default=0)

    def __str__(self):
        return f"{self.order_id} | {self.product_id}"

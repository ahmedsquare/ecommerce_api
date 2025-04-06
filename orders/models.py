# orders/models.py
from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

    def save(self, *args, **kwargs):
        # Calculate the total price based on product price and quantity
        if self.product:
            self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)


from django.db import models
from products.models import Product
from users.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    quantity =  models.PositiveSmallIntegerField(default=0)
    
    def __str__(self) -> str:
        return  f"{self.product.name} : {self.user}"
    
    def subtotal_sum(self):
        return self.product.price * self.quantity

    def total_sum(self):
        return sum(cart.product.price * cart.quantity for cart in Cart.objects.filter(user=self.user))


from django.db import models
from products.models import Product
from users.models import User


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    quantity =  models.PositiveSmallIntegerField(default=0)
    
    def __str__(self) -> str:
        return  f"{self.product.name} : {self.user}"
    
    def total_sum(self):
        return self.product.price * self.quantity
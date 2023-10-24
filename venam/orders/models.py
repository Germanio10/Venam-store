from django.db import models

from users.models import User


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=40)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    initiator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

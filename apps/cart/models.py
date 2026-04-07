from django.db import models
from apps.core.models import BaseModel
from apps.users.models import User
from apps.products.models import Product

class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrinho de {self.user.username}"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
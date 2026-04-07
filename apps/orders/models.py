from django.db import models
from apps.core.models import BaseModel
from apps.users.models import User
from apps.products.models import Product

class Order(BaseModel):
    STATUS_CHOICES = (
        ('PENDING', 'Pendente'),
        ('PAID', 'Pago'),
        ('DELIVERED', 'Entregue'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Pedido {self.id} - {self.user.username}"


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"